# Browser Automation with AI Model

A robust browser automation setup that integrates AI model for intelligent web interactions. This application takes user input and executes complex tasks on a Chromium browser using advanced AI reasoning.

## Key Features

- **Persistent Browser Sessions**: Browser stays open between tasks for better performance
- **Intelligent Task Execution**: Uses Google's Gemini 2.0 Flash model for smart web automation
- **User-Friendly Interface**: Terminal-based menu system with clear options
- **Robust Error Handling**: Graceful error recovery and browser session management
- **API Key Management**: Secure storage and validation of API keys
- **Cross-Platform Support**: Works on Linux, macOS, and Windows

## Recent Improvements

### ✅ Fixed Issues:
- **Browser Persistence**: Browser now properly stays open between tasks
- **Memory Management**: Improved browser session handling to prevent memory leaks
- **Error Recovery**: Better error handling with option to reset browser sessions
- **Signal Handling**: Graceful shutdown on Ctrl+C or system signals
- **API Key Validation**: Enhanced validation for Google API keys
- **Dependency Management**: Automatic installation of required Playwright browsers

### 🚀 New Features:
- **Browser Session Manager**: Centralized management of browser instances
- **Reset Browser Option**: Ability to reset browser session without restarting app
- **Startup Script**: Automated setup and dependency checking
- **Enhanced Logging**: Better status messages and progress indicators
- **Graceful Shutdown**: Proper cleanup of resources on exit

## System Requirements

- **Operating System**: Linux, macOS, or Windows with GUI support
- **Python**: 3.8 or higher
- **Memory**: At least 2GB RAM (4GB recommended)
- **Display**: GUI environment (required for browser display)

## Installation & Setup

### Quick Start (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd browser-automation-ai
   ```

2. **Run the setup script**:
   ```bash
   # For Ubuntu/Debian:
   ./setup-debian.sh
   
   # For Arch Linux:
   ./setup-arch.sh
   ```

3. **Start the application**:
   ```bash
   ./start.sh
   ```

### Manual Setup

1. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**:
   ```bash
   playwright install chromium
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

### First Time Setup

1. **Get Google API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key for use in the application

2. **Start the application**:
   ```bash
   ./start.sh  # or python main.py
   ```

3. **Add your API key**:
   - Select option "2. Manage API Keys"
   - Choose "1. Add/Update Google API Key"
   - Paste your API key when prompted

### Running Tasks

1. **Select "1. Run Task"** from the main menu
2. **Enter your task** in natural language, for example:
   - "Go to Google and search for Python tutorials"
   - "Navigate to GitHub and find trending repositories"
   - "Open YouTube and search for AI tutorials"
   - "Visit Amazon and search for laptops under $1000"

3. **Watch the AI execute** your task in the browser
4. **Browser stays open** for your next task

### Menu Options

- **Run Task**: Execute a new automation task
- **Manage API Keys**: Add, test, or remove API keys
- **Reset Browser Session**: Restart browser if issues occur
- **Close Browser**: Close browser but keep app running
- **Exit**: Gracefully shutdown application

## Advanced Features

### Browser Session Management

The application maintains a persistent browser session that:
- Stays open between tasks for faster execution
- Maintains cookies and session data
- Can be reset if issues occur
- Automatically cleans up on exit

### Error Recovery

If a task fails, the application:
- Provides detailed error information
- Offers to reset the browser session
- Maintains stability for subsequent tasks
- Logs errors for debugging

### API Key Security

API keys are:
- Stored securely in your home directory (`~/.browser_use/api_keys.json`)
- Validated before use
- Never displayed in full in the interface
- Can be easily updated or removed

## Troubleshooting

### Common Issues

1. **"No module named 'browser_use'"**:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **"Playwright browser not found"**:
   ```bash
   playwright install chromium
   ```

3. **API key errors**:
   - Verify your API key at [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Use "Test Current API Key" option in the menu

4. **Browser won't start**:
   - Ensure you have a GUI environment
   - Try resetting the browser session
   - Check system resources (memory/CPU)

### Performance Tips

- **Keep browser open**: Don't close between tasks for better performance
- **Monitor memory**: Reset browser session if memory usage is high
- **Use specific tasks**: More specific instructions yield better results
- **Check API limits**: Monitor your Google API usage

## Development

### Project Structure

```
browser-automation-ai/
├── main.py              # Main application with improved browser management
├── api_manager.py       # Enhanced API key management
├── config.py           # Configuration settings
├── start.sh            # Startup script with dependency checking
├── requirements.txt    # Python dependencies
├── setup-debian.sh     # Ubuntu/Debian setup script
├── setup-arch.sh       # Arch Linux setup script
└── README.md          # This file
```

### Key Improvements Made

1. **BrowserManager Class**: Centralized browser session management
2. **Signal Handlers**: Proper cleanup on interruption
3. **Enhanced Error Handling**: Better recovery from failures
4. **API Key Validation**: Format checking and validation
5. **Startup Script**: Automated dependency management
6. **Memory Management**: Proper resource cleanup

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Acknowledgments

- Built using [browser-use](https://github.com/browser-use/browser-use) library
- Powered by Google's Gemini 2.0 Flash model
- Inspired by the original browser-use project

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are installed
3. Verify your API key is valid
4. Try resetting the browser session

For additional help, please create an issue in the repository with:
- Your operating system
- Python version
- Error messages (if any)
- Steps to reproduce the issue