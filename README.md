# Browser Automation with AI Models

A minimal browser automation setup that integrates AI models. Built using Windsurf Code editor.
Original code: https://github.com/browser-use

## System Requirements
Tested on:
- OS: Ubuntu 24.04 LTS
- Python: 3.12
- Playwright: Latest

## Configured AI Models
At least one API key required:
- GROQ (Mixtral) - https://console.groq.com
- Anthropic Claude - https://console.anthropic.com
- Google Gemini - https://makersuite.google.com
- OpenRouter Mistral - https://openrouter.ai
- DeepSeek - https://platform.deepseek.com

## Installation
Three commands to get started:
```bash
git clone https://github.com/yourusername/browser-use-shell.git
```
```bash
cd browser-use-shell
```
```bash
bash setup.sh
```

## User Inputs During Setup
1. LLM API Keys (at least one required)
   - Skip any key by pressing Enter
   - Keys are saved in `.env` file
   - Edit later using: `nano .env`

2. Model Selection
   - Choose from available models
   - Enter the number of your choice

3. Task Input
   - Enter your automation task
   - Example: "Go to Google and search for Python"
   - Task progress shown in terminal
   - Results saved as GIF

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
- `setup.sh`: Installation and configuration
- `config.py`: AI model settings
- `test_models.py`: API connectivity tests
- `main.py`: Browser automation
- `requirements.txt`: Python dependencies
- `.env`: API keys (created during setup)
- `agent_history.gif`: Task recording
