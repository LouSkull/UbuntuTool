# UbuntuTool
# Linux Tools Script

A Python script to manage various tasks on a Linux system, including package management, disk usage, file management, development tools installation, and network tools.

## Features

1. **Install .deb Package**: Install a .deb package using `dpkg`.
2. **Extract tar.gz File** (In Development): Extract tar.gz files.
3. **List Installed Packages**: List all installed packages using `dpkg --list`.
4. **Remove Application**: Remove an application using `apt-get`.
5. **Disk Usage and File Management**: 
    - Get disk usage statistics.
    - List large files in a directory.
    - Clean temporary files in a specified directory.
6. **Development Tools**: Install common development tools like Git, Vim, and GCC.
7. **Network Tools**: 
    - Check the current IP address.
    - Ping a host.
    - Check network status.

## Requirements

- Python 3.x
- Linux operating system

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LouSkull/UbuntuTool.git
    cd linux-tools-script
    ```

2. Make the script executable:
    ```bash
    chmod +x main.py
    ```

3. Install necessary dependencies (if any).

## Usage

Run the script:
```bash
python3 main.py
```
Follow the on-screen instructions to use the various tools provided.
# Menu Options
[+] Main Menu:
[+] 1. Install .deb Package
[+] 2. Extract tar.gz File (In Development)
[+] 3. List Installed Packages
[+] 4. Remove Application
[+] 5. Disk Usage and File Management
[+] 6. Development Tools
[+] 7. Network Tools
[+] 8. Exit

[+] Disk Usage and File Management:
[+] 1. Get Disk Usage
[+] 2. List Large Files
[+] 3. Clean Temporary Files
[+] 4. Back to Main Menu

[+] Development Tools:
[+] 1. Install Git
[+] 2. Install Vim
[+] 3. Install GCC
[+] 4. Back to Main Menu

[+] Network Tools:
[+] 1. Check IP Address
[+] 2. Ping Host
[+] 3. Check Network Status
[+] 4. Back to Main Menu

