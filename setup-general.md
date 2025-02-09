# Windows Installation Guide

This guide provides step-by-step instructions for setting up the project on Windows. 
Follow these steps carefully to ensure proper installation.

## Prerequisites

1. **Disk Space**: At least 500MB free space
2. **Permissions**: Administrator access

## Installation Methods

### Method 1: Using Git (Recommended)

1. Open Command Prompt as Administrator
2. Install Git:
   ```
   winget install --id Git.Git -e --source winget
   ```
3. Clone the repository:
   ```
   git clone https://github.com/kadavilrahul/browser-use-shell.git
   ```
4. Navigate to the project directory:
   ```
   cd browser-use-shell
   ```

## Post-Installation Steps

1. Install Python (if required):
   ```
   winget install Python.Python.3.11
   ```
   ```
   python --version
   ```

2. Set up Virtual Environment:
   ```
   python -m venv venv
   ```
   ```
   .\venv\Scripts\activate
   ```

3. Install project dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install Playwright and browsers:
   ```
   python -m playwright install
   ```
   ```
   python -m playwright install-deps
   ```

5. Run the application:
   ```
   python main.py
   ```

## Troubleshooting

- **Permission Errors**: Run Command Prompt as Administrator
- **Missing Dependencies**: Check requirements.txt and install missing packages
- **Git Issues**: Ensure Git is properly installed and added to PATH

For additional help, refer to the [README.md](README.md) file or open an issue on GitHub.
