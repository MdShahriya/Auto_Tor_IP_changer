# -*- coding: utf-8 -*-

import time
import os
import subprocess
import sys

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

try:
    print_status("Checking for required packages...", "info")
    import requests
except Exception:
    print_status("python3 requests is not installed", "warning")
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print_status("python3 requests is installed", "success")

try:
    print_status("Checking if Tor is installed...", "info")
    check_tor = subprocess.check_output('which tor', shell=True)
    print_status("Tor is already installed", "success")
except subprocess.CalledProcessError:
    print_status("Tor is not installed!", "error")
    print_status("Installing Tor...", "info")
    try:
        subprocess.check_output('sudo apt update',shell=True)
        subprocess.check_output('sudo apt install tor -y',shell=True)
        print_status("Tor installed successfully", "success")
    except subprocess.CalledProcessError as e:
        print_status(f"Failed to install Tor: {str(e)}", "error")
        print_status("Please install Tor manually using: sudo apt install tor", "warning")
        sys.exit(1)

# Clear screen based on OS
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

def ma_ip():
    url='http://checkip.amazonaws.com'
    try:
        get_ip = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'), timeout=10)
        return get_ip.text.strip()
    except requests.exceptions.ConnectionError:
        return "Error: Connection refused. Tor service may not be running properly."
    except requests.exceptions.Timeout:
        return "Error: Connection timed out. Tor network might be slow or unreachable."
    except Exception as e:
        return f"Error: {str(e)}"

def check_tor_running():
    """Check if Tor service is running"""
    try:
        # Try both systemctl and service commands
        if sys.platform.startswith('linux'):
            try:
                # First try systemctl (modern Linux distros including Kali)
                result = subprocess.run(['systemctl', 'is-active', 'tor'], 
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if 'active' in result.stdout:
                    return True
            except:
                # Fall back to service command
                result = subprocess.run(['service', 'tor', 'status'], 
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if 'running' in result.stdout:
                    return True
        return False
    except:
        return False

def start_tor_service():
    """Start the Tor service using the appropriate command"""
    print_status("Starting Tor service...", "info")
    try:
        if sys.platform.startswith('linux'):
            # Try systemctl first (modern Linux distros including Kali)
            try:
                subprocess.run(['sudo', 'systemctl', 'start', 'tor'], check=True)
            except:
                # Fall back to service command
                subprocess.run(['sudo', 'service', 'tor', 'start'], check=True)
        else:
            os.system("service tor start")
            
        # Verify Tor is running
        if check_tor_running():
            print_status("Tor service started successfully", "success")
            return True
        else:
            print_status("Failed to start Tor service", "error")
            return False
    except Exception as e:
        print_status(f"Error starting Tor service: {str(e)}", "error")
        return False

def change():
    print_status("Reloading Tor service...", "info")
    try:
        if sys.platform.startswith('linux'):
            # Try systemctl first (modern Linux distros including Kali)
            try:
                subprocess.run(['sudo', 'systemctl', 'reload', 'tor'], check=True)
            except:
                # Fall back to service command
                subprocess.run(['sudo', 'service', 'tor', 'reload'], check=True)
        else:
            os.system("service tor reload")
            
        # Wait a moment for Tor to establish connections
        time.sleep(2)
        
        new_ip = ma_ip()
        if new_ip.startswith("Error"):
            print_status(f"{new_ip}", "error")
            print_status("Attempting to restart Tor service...", "warning")
            if start_tor_service():
                time.sleep(3)  # Give it time to establish connections
                new_ip = ma_ip()
                if not new_ip.startswith("Error"):
                    print_status(f"Your IP has been changed to: {new_ip}", "success")
                else:
                    print_status("Failed to connect through Tor after restart", "error")
        else:
            print_status(f"Your IP has been changed to: {new_ip}", "success")
    except Exception as e:
        print_status(f"Error changing IP: {str(e)}", "error")

# Display a more visually appealing banner
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
║         {COLORS['YELLOW']}Made by mrFD{COLORS['GREEN']}              ║
║         {COLORS['YELLOW']}Enhanced by TOPAY{COLORS['GREEN']}         ║
╚══════════════════════════════════════════════════════════════════════╝{COLORS['RESET']}
'''  
print(banner)

colored_print('CYAN', "Follow: http://facebook.com/ninja.hackerz.kurdish/\n")
colored_print('CYAN', "Follow: https://x.com/TopayFoundation/\n")

# Start Tor service with visual feedback
if not start_tor_service():
    print_status("Could not start Tor service. Please check your installation.", "error")
    print_status("Try running: sudo service tor start", "info")
    print_status("Or: sudo systemctl start tor", "info")
    sys.exit(1)

# Loading animation
print_status("Initializing connection", "info")
for _ in range(5):
    sys.stdout.write(f"{COLORS['YELLOW']}.{COLORS['RESET']}")
    sys.stdout.flush()
    time.sleep(0.5)
print("\n")

# Test Tor connection
test_ip = ma_ip()
if test_ip.startswith("Error"):
    print_status(f"Failed to connect through Tor: {test_ip}", "error")
    print_status("Please check if Tor service is running correctly", "warning")
    print_status("You can try manually restarting Tor with: sudo service tor restart", "info")
    print_status("Or: sudo systemctl restart tor", "info")
    sys.exit(1)
else:
    print_status(f"Successfully connected through Tor. Your current IP: {test_ip}", "success")

# Important proxy information with better visibility
proxy_info = f'''{COLORS['GREEN']}┌───────────────────────────────────────┐
│ {COLORS['YELLOW']}IMPORTANT: Configure your application to │
│ use SOCKS proxy: {COLORS['CYAN']}127.0.0.1:9050{COLORS['YELLOW']}        │
{COLORS['GREEN']}└───────────────────────────────────────┘{COLORS['RESET']}'''
print(proxy_info)

# Improved user input with default values and validation
while True:
    x_input = input(f"{COLORS['GREEN']}[+]{COLORS['RESET']} Time to change IP in seconds {COLORS['YELLOW']}[default=60]{COLORS['RESET']} >> ")
    x = x_input if x_input.strip() else "60"
    if x.isdigit() and int(x) > 0:
        break
    print_status("Please enter a valid positive number", "error")

lin_input = input(f"{COLORS['GREEN']}[+]{COLORS['RESET']} How many times to change IP? {COLORS['YELLOW']}[Enter for infinite]{COLORS['RESET']} >> ")
lin = lin_input if lin_input.strip() else "0"

try:
    lin = int(lin)
    x_seconds = int(x)
    
    # Display current IP before starting
    print_status("Your current Tor IP address", "info")
    current_ip = ma_ip()
    colored_print('CYAN', f"Current IP: {current_ip}\n")
    
    if lin == 0:
        # Infinite mode with better visual feedback
        colored_print('PURPLE', "┌─ Starting infinite IP change mode ─┐")
        colored_print('PURPLE', "│  Press Ctrl+C to stop the process  │")
        colored_print('PURPLE', "└────────────────────────────────────┘")
        
        counter = 1
        while True:
            try:
                # Progress indicator
                for i in range(x_seconds):
                    remaining = x_seconds - i
                    sys.stdout.write(f"\r{COLORS['YELLOW']}[*] Next IP change in: {remaining} seconds {COLORS['RESET']}")
                    sys.stdout.flush()
                    time.sleep(1)
                print("\n")
                
                # Change IP with counter
                print_status(f"Changing IP (#{counter})", "info")
                change()
                counter += 1
                
            except KeyboardInterrupt:
                print_status("\nAuto IP changer has been stopped", "warning")
                break
    else:
        # Limited mode with progress tracking
        colored_print('PURPLE', f"┌─ Starting IP change: {lin} times ─┐")
        colored_print('PURPLE', "└────────────────────────────────────┘")
        
        for i in range(1, lin + 1):
            # Progress indicator
            for j in range(x_seconds):
                remaining = x_seconds - j
                progress = f"[{i}/{lin}]" 
                sys.stdout.write(f"\r{COLORS['YELLOW']}[*] {progress} Next IP change in: {remaining} seconds {COLORS['RESET']}")
                sys.stdout.flush()
                time.sleep(1)
            print("\n")
            
            # Change IP with counter
            print_status(f"Changing IP (#{i}/{lin})", "info")
            change()
            
        print_status(f"Completed {lin} IP changes successfully", "success")

except ValueError:
    print_status("Invalid input. Please enter a valid number.", "error")

print_status("Thank you for using Auto Tor IP Changer!", "success")
