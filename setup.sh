#!/bin/bash

# Exit on any error
set -e

echo "Starting setup process..."

# 1. Update system and install dependencies
echo "Installing system dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

# 2. Create and activate virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 3. Verify virtual environment
PYTHON_PATH=$(which python3)
if [[ $PYTHON_PATH != *"venv"* ]]; then
    echo "Error: Virtual environment not activated correctly"
    exit 1
fi
echo "Virtual environment activated successfully at: $PYTHON_PATH"

# 4. Install Python packages
echo "Installing Python packages..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# 5. Install Playwright and browsers
echo "Installing Playwright and browsers..."
python3 -m playwright install
python3 -m playwright install-deps

# 6. Verify installations
echo "Verifying installations..."
echo "Python version:"
python3 --version
echo "Pip version:"
python3 -m pip --version
echo "Playwright version:"
python3 -m playwright --version
echo "Installed packages:"
python3 -m pip list

# 7. Setup environment file and collect API keys
echo "Setting up environment file..."

# Create .env file
echo "# API Keys Configuration" > .env

# Function to prompt for API key
get_api_key() {
    local key_name="$1"
    local description="$2"
    local api_key=""
    
    while [ -z "$api_key" ]; do
        echo ""
        echo "$description"
        read -p "Enter $key_name (press Enter to skip): " api_key
        if [ -z "$api_key" ]; then
            echo "Skipping $key_name..."
            return
        fi
    done
    echo "$key_name=$api_key" >> .env
}

# Collect API keys
echo "Please enter your API keys. Press Enter to skip any you don't have."

get_api_key "GROQ_API_KEY" "Groq API Key (for Mixtral model)"
get_api_key "ANTHROPIC_API_KEY" "Anthropic API Key (for Claude model)"
get_api_key "GOOGLE_API_KEY" "Google API Key (for Gemini model)"
get_api_key "OPENROUTER_API_KEY" "OpenRouter API Key (for Mistral model)"
get_api_key "DEEPSEEK_API_KEY" "DeepSeek API Key"

echo ""
echo "API keys have been saved to .env file"
echo "You can edit them later using: nano .env"

# 8. Run tests with API keys
echo ""
echo "Running tests with provided API keys..."
python3 test_models.py

echo "Setup completed successfully!"
echo "To activate the virtual environment in new terminals, use: source venv/bin/activate"

# 9. Ask user if they want to run the main script
echo ""
read -p "Do you want to start the browser automation now? (y/n): " start_automation

if [[ $start_automation == "y" || $start_automation == "Y" ]]; then
    echo "Starting browser automation..."
    python3 main.py
else
    echo "You can start the browser automation later by running: python3 main.py"
fi
