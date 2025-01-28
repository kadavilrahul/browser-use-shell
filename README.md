# Browser Automation with AI Models

A minimal browser automation setup that integrates AI models. Built using Windsurf Code editor. 
It opens a chromium browser, navigates to a website, and performs tasks like login, search, and data extraction.
This is simplified and modified version of the original code: https://github.com/browser-use
You may also install Chrome remote desktop to test the automation on a remote Ubuntu machine using the repo https://github.com/kadavilrahul/chrome_remote_desktop

## System Requirements
- Tested on OS: Ubuntu 24.04 LTS
- Python: 3.12
- Playwright: Latest
- This code may work well with other Linux distros also

## Configured AI Models
At least one API key required:
- GROQ (Free API) - https://console.groq.com
- Anthropic Claude - https://console.anthropic.com
- Google Gemini (Free API) - https://aistudio.google.com/
- OpenRouter Mistral - https://openrouter.ai
- DeepSeek - https://platform.deepseek.com

## Installation
Run these commands on Linux terminal to get started:
```bash
git clone https://github.com/kadavilrahul/browser-use-shell.git
```
```bash
cd browser-use-shell
```
```bash
bash setup.sh
```

## User Inputs During Setup
1. LLM API Keys (at least one required)
    - Enter your API keys one by one
    - Skip any key by pressing Enter


2. Model Selection
   - Choose from available models (numbered list)
   - Free models are marked with [Free]
   - Recommended for beginners: Google Gemini or GROQ

3. Task Input
   - Enter your automation task and follow on-screen instructions
   - Example tasks:
     ```
     "Go to wordpress order section of xxxx.com, ID:xxxx Password:xxxx and search for latest orders"
     "Login to GitHub with username:xxx password:xxx and check notifications"
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
