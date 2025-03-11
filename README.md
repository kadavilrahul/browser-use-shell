# Browser Automation with AI Model

- A minimal browser automation setup that integrates AI model
- It takes user input and executes tasks on a Chromium browser
- Built using Windsurf Code editor and Claude 3.5 Sonnet model
- This is simplified and modified version of the original code: https://github.com/browser-use

#### Modifications and improvement done
- The tool will be ready to use by running two commands on terminal
- Made it user friendly by adding user inputs on terminal for all the tasks
- Used only one LLM model for now to avoid API format errors
- Keeps browser open after task completion unless exit is done
- New tasks can be executed after current one is completed on already open brower

#### System Requirements
- A system with GUI (GUI is needed only to access browser)
- Python

#### Tested on OS: 
-  Ubuntu 24.04 LTS
-  Garuda Linux (Rolling)
-  Windows 10 Pro 64-bit

#### Note: 
- Use any IDE with AI support to modify code as per your use.
- If you are working on a remote Linux headless machine then you will need a GUI and remote desktop connection to access browser. You can install Chrome remote desktop on a remote Ubuntu machine using this repo https://github.com/kadavilrahul/chrome_remote_desktop

#### Configured AI Models
At least one API key required:
- Google Gemini (Free API) - https://aistudio.google.com/apikey
- Configured Gemini model is "gemini-2.0-flash-exp"

## Setup and Installation 
### Linux: 
(Run these commands on Linux terminal to get started)
 - Enter desired folder location. Modify command with correct folder name
```bash
cd /path/to/your/folder
```
 - Git clone and enter repository folder 
```bash
git clone https://github.com/kadavilrahul/browser-use-shell.git && cd browser-use-shell && bash main.sh
```

 - Run the code after installation to start using browser use shell
```bash
source venv/bin/activate && python main.py
```
### Windows:
(Run these commands on Windows terminal (Powershell) or system terminal to get started)
 - Enter desired folder location. Modify command with correct folder name
```powershell
cd Path\To\Your\Folder
```
 - Git clone and enter repository folder
```powershell
git clone https://github.com/kadavilrahul/browser-use-shell.git; cd browser-use-shell; python -m venv venv; .\venv\Scripts\activate; pip install -r requirements.txt; python main.py
```
 - Rerun the code after installation
```powershell
.\venv\Scripts\Activate; python main.py
```

If error comes
- Check if python is installed
- Open PowerShell as Administrator and run below command to approve execution policy
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- Run commands one by one
  ```
  git clone https://github.com/kadavilrahul/browser-use-shell.git
  ```
  cd browser-use-shell
  ```
  ```
  python -m venv venv
  ```
  ```
  .\venv\Scripts\activate
  ```
  ```
  pip install -r requirements.txt
  ```
  ```
  python main.py
  ```
  
  
#### User Inputs During Setup
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

#### Manual Python Usage
Start automation:
```
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
