# ⚙️ Setup & Usage Guide – Secure Data Wiping System

---

## 📌 Overview

This guide helps you run the Secure Data Wiping System on your computer.  
The system detects storage devices, shows recoverable files, securely wipes selected files, and verifies deletion.

---

## 📥 Step 1: Download the Project

1. Go to the GitHub repository  
2. Click **Code → Download ZIP**  
3. Extract the ZIP file to your Desktop  

---

## 🖥️ Step 2: Open Command Prompt (IMPORTANT)

1. Press `Windows + R`  
2. Type `cmd`  
3. Right-click on Command Prompt  
4. Click **Run as Administrator**

⚠️ Administrator access is required for device detection and recovery scanning.

---

## 📂 Step 3: Navigate to Project Folder

```bash
cd /d "C:\Users\YourUsername\Desktop\secure-wipe-system"


▶️ Step 4: Run the Program
python device_monitor.py


⚙️ Step 5: Automatic Setup (First Run Only)

When running for the first time:

Required libraries will be installed automatically
You will see messages like:
Installing required packages...
Please wait...

⚠️ Do NOT close the program during installation

🔌 Step 6: Connect Storage Device
Insert a USB drive / external storage device
The system will automatically detect it

📊 Step 7: Follow On-Screen Instructions

You will be prompted to:

Choose file source:
Device Files
Recoverable Files
Select category (if recoverable files)
Select file number
Confirm deletion:
Are you sure you want to erase this file? (y/n)


🔐 Step 8: Secure Wipe Process

The system will:

Perform multi-pass overwrite
Delete the file securely
Verify deletion using hash comparison


🤖 Step 9: ML-Based Analysis

After wiping, the system will:

Run recovery scan again
Compare before/after results
Generate:
Recoverability Score
Security Level
Prediction


🔍 Step 10: Final Verification

You will see:

Fully erased
Partially recoverable
Still recoverable
📄 Output Files

After execution, the following files are generated:

📄 Certificate
certificate.pdf
Proof of secure deletion
Automatically opens after generation
📝 Logs
logs.txt

Contains:

Selected file
Wipe process
ML results
Final status
⚠️ Important Notes
Always run as Administrator
Internet is required only for first run
Do NOT remove USB during scanning or wiping
Do NOT interrupt the program during execution
❌ Common Issues & Fixes
🔹 Device not detected
Try reconnecting USB
Use a different port
🔹 Permission error
Ensure Command Prompt is running as Administrator
🔹 Recovery scan not working
Ensure testdisk-7.2 folder exists in project directory
🔹 Program seems stuck
Wait during recovery scan (it may take time)
🚀 You’re Done!

You have successfully run the Secure Data Wiping System 🎉

👨‍💻 Author

Pramod M R
