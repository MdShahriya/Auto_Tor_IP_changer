# Auto Tor IP Changer v2.5

![Version](https://img.shields.io/badge/Version-2.5-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Linux-blue%20%7C)

## 🌐 Overview

Auto Tor IP Changer is a powerful tool that automatically changes your IP address at specified intervals using the Tor network. This provides enhanced privacy and anonymity while browsing the internet or performing network operations.

## ✨ Features

- 🔄 Automatic IP rotation at customizable intervals
- 🔢 Set specific number of IP changes or run in infinite mode
- 🖥️ Cross-platform support (Linux and Windows)
- 📊 Visual progress tracking and status updates
- 🔌 Easy SOCKS proxy configuration (127.0.0.1:9050)
- 🛡️ Enhanced privacy and anonymity

## 📋 Prerequisites

- Python 3.x
- Tor service
- Python requests library with SOCKS support

> **Note:** The installer will automatically check for and install these requirements if they're missing.

## 🔧 Installation

### Automatic Installation

1. Clone the repository:

   ```
   git clone https://github.com/TOPAY-FOUNDATION/Auto_Tor_IP_changer.git
   ```

2. Navigate to the project directory:

   ```
   cd Auto_Tor_IP_changer
   ```

3. Run the installer script:

   ```
   python3 install.py
   ```

4. Follow the on-screen instructions to complete the installation.

### Platform-Specific Instructions

#### Linux

After installation, you can start the tool from anywhere by typing:

```
aut
```

## 🚀 Usage

1. Start the tool using the appropriate command for your platform.

2. Enter the time interval (in seconds) between IP changes (default: 60).

3. Enter how many times you want to change your IP:
   - Enter a specific number for limited changes
   - Press Enter (or input 0) for infinite IP changes

4. Configure your applications to use the SOCKS proxy:
   - Address: 127.0.0.1
   - Port: 9050

5. Enjoy your automatic IP changes! Press Ctrl+C to stop the process at any time.

## 🔍 Troubleshooting

- If you encounter any issues with Tor connectivity, ensure the Tor service is properly installed and running.
- For proxy connection issues, verify that your application is correctly configured to use the SOCKS5 proxy (127.0.0.1:9050).

## 👨‍💻 Contributors

- Created by [mrFD](http://facebook.com/ninja.hackerz.kurdish/)
- Enhanced by [TOPAY](https://x.com/TopayFoundation/)

## 📜 License

This project is open source and available under the MIT License.
