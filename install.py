# -*- coding: utf-8 -*-

import os
import sys
import time

# Color codes for better visual output
COLORS = {
    'BLUE': '\033[1;34;40m',
    'GREEN': '\033[1;32;40m',
    'RED': '\033[1;31;40m',
    'YELLOW': '\033[1;33;40m',
    'PURPLE': '\033[1;35;40m',
    'CYAN': '\033[1;36;40m',
    'WHITE': '\033[1;37;40m',
    'RESET': '\033[0m'
}

# Print colored text
def colored_print(color, text):
    print(f"{COLORS[color]}{text}{COLORS['RESET']}")

# Print status messages
def print_status(message, status_type='info'):
    if status_type == 'info':
        colored_print('BLUE', f"[*] {message}")
    elif status_type == 'success':
        colored_print('GREEN', f"[+] {message}")
    elif status_type == 'error':
        colored_print('RED', f"[!] {message}")
    elif status_type == 'warning':
        colored_print('YELLOW', f"[!] {message}")

# Clear screen based on OS
def clear_screen():
    os.system('clear')

# Display a visually appealing banner
banner = fr'''{COLORS['GREEN']}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                            _          _______                        ║
║                 /\        | |        |__   __|                       ║
║                /  \  _   _| |_ ___      | | ___  _ __                ║
║               / /\ \| | | | __/ _ \     | |/ _ \| '__|               ║
║              / ____ \ |_| | || (_) |    | | (_) | |                  ║
║             /_/    \_\__,_|\__\___/     |_|\___/|_|                  ║
║                                                                      ║
║      {COLORS['CYAN']}Auto IP Changer v2.5{COLORS['GREEN']}           ║
║      {COLORS['YELLOW']}Made by mrFD{COLORS['GREEN']}                                   ║
║      {COLORS['YELLOW']}Enhanced by TOPAY{COLORS['GREEN']}                              ║
╚══════════════════════════════════════════════════════════════════════╝{COLORS['RESET']}
'''

# Function to show progress animation
def show_progress(message, duration=2.0):
    symbols = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        i = (i + 1) % len(symbols)
        print(f"\r{COLORS['CYAN']}[{symbols[i]}] {message}{COLORS['RESET']}", end='')
        time.sleep(0.1)
    print()

# Check if running as administrator/root
def is_admin():
    # Check for root privileges on Linux
    return os.geteuid() == 0

# Main function
def main():
    clear_screen()
    print(banner)
    
    # Check for admin privileges
    if not is_admin():
        print_status("This script requires administrator privileges to install/uninstall", "error")
        print_status("Please run this script as administrator/root", "info")
        sys.exit(1)
    
    # Set up for Linux
    run = os.system
    
    # Installation/Uninstallation choice
    colored_print('CYAN', "Welcome to Auto Tor IP Changer Installer")
    print()
    colored_print('YELLOW', "[1] Install Auto Tor IP Changer")
    colored_print('YELLOW', "[2] Uninstall Auto Tor IP Changer")
    colored_print('RED', "[3] Exit")
    print()
    
    while True:
        choice = input(f"{COLORS['GREEN']}[?] Please select an option (1-3): {COLORS['RESET']}")
        
        if choice == '1':
            # Installation process
            print_status("Starting installation process...", "info")
            
            # Linux installation
            print_status("Installing for Linux...", "info")
            show_progress("Setting up permissions", 1)
            run('chmod 777 autoTOR.py')
            
            show_progress("Creating directories", 1)
            run('mkdir -p /usr/share/aut')
            
            show_progress("Copying files", 1)
            run('cp autoTOR.py /usr/share/aut/autoTOR.py')
            
            show_progress("Creating executable", 1)
            cmnd = ('#! /bin/sh\nexec python3 /usr/share/aut/autoTOR.py "$@"')
            with open('/usr/bin/aut', 'w') as file:
                file.write(cmnd)
                
            show_progress("Setting permissions", 1)
            run('chmod +x /usr/bin/aut && chmod +x /usr/share/aut/autoTOR.py')
            
            print_status("Auto Tor IP Changer has been installed successfully!", "success")
            print_status("You can now run it by typing 'aut' in terminal", "info")
            colored_print('GREEN', "\nType 'aut' in terminal to start Auto Tor IP Changer")
            
            break
            
        elif choice == '2':
            # Uninstallation process
            print_status("Starting uninstallation process...", "info")
            
            # Linux uninstallation
            print_status("Uninstalling from Linux...", "info")
            show_progress("Removing files", 2)
            run('rm -r /usr/share/aut')
            run('rm /usr/bin/aut')
            print_status("Auto Tor IP Changer has been uninstalled successfully!", "success")
            
            break
            
        elif choice == '3':
            print_status("Exiting installer...", "info")
            sys.exit(0)
            
        else:
            print_status("Invalid option. Please select 1, 2, or 3.", "error")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print_status("Installation canceled by user", "warning")
        sys.exit(0)
    except Exception as e:
        print_status(f"An error occurred: {str(e)}", "error")
        sys.exit(1)
