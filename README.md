# KEYLOGGER--SSH
KeyShadow 🔐

A proof-of-concept Python keylogger for ethical hacking labs or CTF environments. Logs keystrokes with active window names and securely transmits data to a remote SSH server.

> ⚠️ Disclaimer: This tool is for educational purposes only. Do not use it on machines you do not own or have explicit permission to monitor.




---

🔧 Features

Tracks keystrokes with window context

Sends logs via SSH every 60 seconds

Auto-installs Python and dependencies (Windows)

Simple batch script for automated execution

Cross-platform support (Windows/Linux)



---

🚀 Setup Instructions

1. Clone the Repository

git clone https://github.com/Surya831/KeyShadow.git
cd KeyShadow

2. Windows Setup

Run the batch file:

start_logger.bat

This will:

Install Python (if missing)

Install required dependencies

Start the keylogger minimized


3. Add to Windows Startup

Press Win + R, type: shell:startup
Copy `start_logger.bat` into the opened folder


---

📋 Example Output

[2025-02-22 15:30:00] Active Window: chrome.exe
hello world [Shift] [Enter]

[2025-02-22 15:31:15] Active Window: notepad.exe
this is a test [Backspace] [Backspace] test complete!


---

📦 Files Included

KeyShadow/
├── keylogger.py             # The main Python script
├── start_logger.bat         # Auto-installer & launcher
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── logs/                    # Stores keystroke logs


---

📁 requirements.txt

paramiko
pynput
psutil
pywin32; platform_system == "Windows"


---

✅ Legal Use Only

> You are responsible for all use. This software is intended only for controlled, consensual environments such as ethical hacking labs or cybersecurity education.




---

✨ Credits

Developed by surya831. Pull requests and forks welcome for further development.


---

🌟 License

MIT License. See LICENSE file.

