# Offensive Cyber Security Projects - Python

This repository contains **12 offensive cybersecurity tools** developed in Python as part of a hands-on project series. Each project includes a **Project Description** and a **Solution (code/script)** to 
understand and implement offensive security concepts.

## 🔐 Project List

### 1. Subdomain Enumeration Tool
- **Description**: Understand how to discover subdomains of a target domain using Python.
- **Solution**: Python script that performs subdomain enumeration via wordlists and DNS queries.

### 2. PDF Protection Tool
- **Description**: Learn how to secure PDF files using password protection.
- **Solution**: Python tool to encrypt and protect PDF documents with a user-defined password.

### 3. PDF Cracker Tool
- **Description**: A project focused on cracking password-protected PDFs using brute force/dictionary attacks.
- **Solution**: Script to automate the cracking process using `PyPDF2`.

### 4. Network Scanner
- **Description**: Build a tool to scan live devices on a network.
- **Solution**: Python scanner using ARP requests to identify active IP addresses.

### 5. Port Scanner
- **Description**: Scan for open ports on a specific host to detect exposed services.
- **Solution**: A multithreaded Python script to perform TCP port scans.

### 6. Password Cracker
- **Description**: Crack hashed or encrypted passwords using a dictionary attack.
- **Solution**: Python code that compares hashed values against a list of potential passwords.

### 7. SSH Cracker
- **Description**: Brute-force SSH login using a username-password list.
- **Solution**: Script using `paramiko` to test SSH login credentials.

### 8. FTP Cracker
- **Description**: Brute-force attack on FTP servers to gain unauthorized access.
- **Solution**: Python script to test login combinations using `ftplib`.

### 9. Backdoor [Reverse Shell]
- **Description**: Develop a Python backdoor to establish a reverse shell connection.
- **Solution**: Script that connects back to an attacker’s system and executes remote commands.

### 10. Information Stealer
- **Description**: Tool to extract system info, credentials, clipboard data, and more.
- **Solution**: A modular Python script that simulates info-stealing malware.

### 11. SSH Botnet
- **Description**: Learn how to build a simple SSH-based botnet controller.
- **Solution**: A script to send commands to multiple infected systems via SSH.

---

## ⚙️ Project Prerequisites

To run these projects, you’ll need:

- Python 3.x
- Required Python packages:  
  - `paramiko`  
  - `socket`  
  - `os`, `sys`, `subprocess`  
  - `ftplib`, `PyPDF2`, `requests`  
  - `scapy`  
  - `colorama` (optional for UI enhancement)  



