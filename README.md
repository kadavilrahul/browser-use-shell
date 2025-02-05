# Browser Automation with AI Models

- A minimal browser automation setup that integrates AI model
- It takes user input and executes tasks on a Chromium browser
- Built using Windsurf Code editor and Claude 3.5 Sonnet model
- This is simplified and modified version of the original code: https://github.com/browser-use

# Modifications and improvement done
- The tool will be ready to use by running two commands on terminal
- Made it user friendly by adding user inputs on terminal for all the tasks
- Used only one LLM model for now to avoid API format errors
- Keeps browser open after task completion unless exit is done
- New tasks can be executed after current one is completed on already open brower

## System Requirements
- Linux system with GUI (GUI is needed only to access browser)

## Tested on OS: 
-  Ubuntu 24.04 LTS
-  Garuda Linux (Rolling)

## Note: 
- This code may work well with other Linux distros also. Use any IDE with AI support to modify code as per your use.
- If you are working on a remote headless machine then you will need a GUI and remote desktop connection to access browser. You can install Chrome remote desktop on a remote Ubuntu machine using this repo https://github.com/kadavilrahul/chrome_remote_desktop

## Configured AI Models
At least one API key required:
- Google Gemini (Free API) - https://aistudio.google.com/apikey
- Configured Gemini model is "gemini-2.0-flash-exp"

## Installation
Run these commands on Linux terminal to get started:
```bash
git clone https://github.com/kadavilrahul/browser-use-shell.git && cd browser-use-shell && bash main.sh
```

## Rerun the code after installation
```bash
source venv/bin/activate && python main.py
```

## User Inputs During Setup
1. LLM API Keys (required)
   - Enter your Gemini API key when prompted
   - Get it from https://aistudio.google.com/apikey

2. Task Input
   - Enter your automation task and follow on-screen instructions
   - Example tasks:
     ```
     Go to wordpress order section of xxxx.com, ID:xxxx Password:xxxx and search for latest orders
     ```
     ```
     Login to GitHub with username:xxx password:xxx and check notifications
     ```
   - Task progress shown in terminal
   - Results saved as GIF in `agent_history.gif`

## Testing
Run tests manually:
```bash
source venv/bin/activate
python test_models.py
```

## Manual Python Usage
Start automation:
```bash
source venv/bin/activate
python main.py
```

## Files
- `setup.sh`: Installation and configuration script
- `config.py`: AI model settings and API configuration
- `test_models.py`: API connectivity tests
- `main.py`: Browser automation script
- `requirements.txt`: Python package dependencies
- `.env`: API keys (created during setup)
- `agent_history.gif`: Visual record of task execution

## Troubleshooting
1. If setup.sh fails:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   playwright install
   ```

2. If browser doesn't open:
   ```bash
   playwright install-deps
   ```

3. If API key errors:
   - Check `.env` file format
   - Ensure no spaces around '=' sign
   - Verify key is active in provider dashboard
