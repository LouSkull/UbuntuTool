import platform
import sys
import os
import time
import shutil


MENU = f"""
 _      _                    _______          _ 
| |    (_)                  |__   __|        | |
| |     _ _ __  _   ___  __    | | ___   ___ | |
| |    | | '_ \\| | | \\ \\/ /    | |/ _ \\ / _ \\| |
| |____| | | | | |_| |>  <     | | (_) | (_) | |
|______|_|_| |_|\\__,_/_/\\_\\    |_|\___/ \\___/|_|
    """
 
CHOICE = "[+] Enter your choice --->  "

MENU_OPTIONS = f"""
Welcome to linux tool! here you can easy control your os! NOTE: This was developed for Ubuntu!
[1] Install \".deb\" Setup - Helps You To Install Apps
[2] Install \"tar.gz\" Setup - Helps You To Install Apps
[3] Apps List - Shows You Every App That You Have Installed
[4] Uninstall App - Uninstall Any App
[5] Disk Usage and File Management - Show Disk Usage And You Can Manage Files
[6] Development Tools - Tools For Developers
[7] Networking - Control Or Show Info Of Your Network
[8] Exit - Terminate Tool
""" 

MENU_OPTIONS2 = """
[1] Get Disk Usage
[2] List Large Files
[3] Clean Temporary Files
[4] Back to Main Menu
"""

DEV_TOOLS_MENU = """
[1] Install Git
[2] Install Vim
[3] Install Gcc
"""

NETWORK_TOOLS_MENU = """
[1] Check IP Address
[2] Ping Host
[3] Check Network Status
[4] Back to Main Menu
"""



def check_os():
    os_name = platform.system()
    if os_name != "Linux":
        print("[+] This application only runs on Linux.")
        sys.exit(1)

def get_disk_usage():
    """Get disk usage statistics."""
    usage = shutil.disk_usage("/")
    print(f"[+] Total: {usage.total // (2**30)} GB")
    print(f"[+] Used: {usage.used // (2**30)} GB")
    print(f"[+] Free: {usage.free // (2**30)} GB")

def list_large_files(directory, size_threshold):
    """List files larger than the specified size in MB."""
    size_threshold_bytes = size_threshold * 1024 * 1024
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > size_threshold_bytes:
                print(f"[+] {file_path}: {os.path.getsize(file_path) / (1024 * 1024):.2f} MB")

def clean_temp_files(temp_directory):
    """Clean up temporary files in the specified directory."""
    for root, dirs, files in os.walk(temp_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"[+] Removed {file_path}")
            except Exception as e:
                print(f"[+] Failed to remove {file_path}: {e}")

def disk_usage_and_file_management():
    while True:
        print(MENU)
        print(MENU_OPTIONS2)
        choice = input(CHOICE)

        if choice == '1':
            get_disk_usage()
        elif choice == '2':
            directory = input("[+] Enter the directory to scan: ")
            size_threshold = int(input("[+] Enter the file size threshold (in MB): "))
            list_large_files(directory, size_threshold)
        elif choice == '3':
            temp_directory = input("[+] Enter the temporary directory to clean: ")
            clean_temp_files(temp_directory)
        elif choice == '4':
            break
        else:
            print("[+] Invalid choice. Please try again.")

def install_development_tool(tool_name):
    """Install a development tool using apt-get."""
    try:
        os.system(f"sudo apt-get install -y {tool_name}")
        print(f"[+] {tool_name} installed successfully.")
    except Exception as e:
        print(f"[+] Error installing {tool_name}: {e}")

def development_tools_menu():
    while True:
        print(DEV_TOOLS_MENU)
        choice = input(CHOICE)

        if choice == '1':
            install_development_tool("git")
        elif choice == '2':
            install_development_tool("vim")
        elif choice == '3':
            install_development_tool("gcc")
        elif choice == '4':
            break
        else:
            print("[+] Invalid choice. Please try again.")

def check_ip_address():
    try:
        os.system("hostname -I")
    except Exception as e:
        print(f"[+] Error checking IP address: {e}")

def ping_host():
    host = input("[+] Enter the host to ping: ")
    try:
        os.system(f"ping -c 4 {host}")
    except Exception as e:
        print(f"[+] Error pinging host: {e}")

def check_network_status():
    try:
        os.system("nmcli general status")
    except Exception as e:
        print(f"[+] Error checking network status: {e}")

def network_tools_menu():
    while True:
        print(NETWORK_TOOLS_MENU)
        choice = input(CHOICE)

        if choice == '1':
            check_ip_address()
        elif choice == '2':
            ping_host()
        elif choice == '3':
            check_network_status()
        elif choice == '4':
            break
        else:
            print("[+] Invalid choice. Please try again.")

def main():
    while True:
        print(MENU)
        print(MENU_OPTIONS)
        choice_input = input(CHOICE)
        
        if choice_input == "1":
            try:
                deb_input_patch = input("[+] Enter path to .deb file --->  ")
                os.system(f"sudo dpkg -i {deb_input_patch}")
                print("[+] Package installed successfully.")
            except Exception as e:
                print(f"[+] Error: {e}")
            time.sleep(2)
        
        elif choice_input == "2":
            # tar_gz_input_patch = input("[+] Enter path --->  ")
            # os.system("")
            print("[+] In Development...")
            time.sleep(2)
            
        elif choice_input == "3":
            os.system("dpkg --list")
            time.sleep(2)
            
        elif choice_input == "4":
            try:
                remove_app_name = input("[+] Enter app name --->  ")
                os.system(f"sudo apt-get remove {remove_app_name}")
                print("[+] Application removed successfully.")
            except Exception as e:
                print(f"[+] Error: {e}")
            time.sleep(2)
            
        elif choice_input == "5":
            disk_usage_and_file_management()
            
        elif choice_input == "6":
            development_tools_menu()
        
        elif choice_input == "7":
            network_tools_menu()
        
        elif choice_input == "8":
            print("[+] Exiting...")
            sys.exit(0)
        
        else:
            print("[+] Invalid choice. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    check_os()
    main()
