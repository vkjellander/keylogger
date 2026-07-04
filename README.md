# Keylogger

An educational keylogger built in Python for cybersecurity research and learning purposes.

## Legal Disclaimer
This tool is for educational purposes only.
Only use on systems you own or have explicit permission to test.
Unauthorized use is illegal and unethical.

## What it does
- Captures keystrokes and logs them to a text file
- Emails the log file to a specified address when stopped
- Available for both Windows and Linux

## Requirements
pip install pynput

## Configuration
Before running, fill in the following variables:

file_path = "path to where you want logs saved"
email_address = "your sender gmail address"
password = "your gmail app password"
toaddr = "email address to receive logs"

## How to get a Gmail App Password
1. Create a throwaway Gmail account
2. Go to myaccount.google.com
3. Enable 2-Step Verification under Security
4. Search for App Passwords
5. Generate one for Mail
6. Use the 16 character password as your password variable

## Usage
Windows:
python keylogger_windows.py

Linux:
python3 keylogger_linux.py

Press ESC to stop the keylogger and send the log file.

## Windows vs Linux Differences
- File paths use \\ on Windows and / on Linux
- Windows version uses raw strings (r"") for file paths
- Both versions use pynput which works cross platform

## What I learned
- How keystroke capture works at OS level
- How pynput hooks into keyboard input on Windows and Linux
- SMTP email sending
