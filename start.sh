#!/bin/bash

# Browser Automation with AI - Startup Script
# This script ensures all dependencies are installed and starts the application

echo "🚀 Browser Automation with AI - Startup"
echo "========================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    echo "   Run: ./setup-debian.sh (for Ubuntu/Debian) or ./setup-arch.sh (for Arch)"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
echo "📦 Checking dependencies..."
python -c "import browser_use, langchain_google_genai" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Install Playwright browsers if needed
echo "🌐 Ensuring Playwright browsers are installed..."
playwright install --with-deps chromium 2>/dev/null || playwright install chromium

# Start the application
echo "🚀 Starting Browser Automation with AI..."
echo ""
python main.py