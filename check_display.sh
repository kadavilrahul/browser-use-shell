#!/bin/bash

echo "🔍 Browser Display Environment Checker"
echo "======================================"

# Check if we're running as root
if [ "$EUID" -eq 0 ]; then
    echo "⚠️  Running as root user"
else
    echo "✅ Running as regular user"
fi

# Check DISPLAY variable
if [ -z "$DISPLAY" ]; then
    echo "❌ DISPLAY environment variable is not set"
    echo "   This means no GUI display is configured"
else
    echo "✅ DISPLAY is set to: $DISPLAY"
fi

# Check if X server is running
if command -v xset >/dev/null 2>&1; then
    if xset q >/dev/null 2>&1; then
        echo "✅ X server is running and accessible"
    else
        echo "❌ X server is not accessible"
    fi
else
    echo "❌ xset command not found (X11 not installed)"
fi

# Check for Xvfb
if command -v xvfb-run >/dev/null 2>&1; then
    echo "✅ Xvfb is available (virtual display)"
else
    echo "❌ Xvfb not found"
    echo "   Install with: sudo apt-get install xvfb"
fi

# Check desktop environment
if [ -n "$XDG_CURRENT_DESKTOP" ]; then
    echo "✅ Desktop environment: $XDG_CURRENT_DESKTOP"
elif [ -n "$DESKTOP_SESSION" ]; then
    echo "✅ Desktop session: $DESKTOP_SESSION"
else
    echo "❌ No desktop environment detected"
fi

echo ""
echo "🎯 RECOMMENDATIONS:"
echo "=================="

if [ -z "$DISPLAY" ]; then
    echo "1. 🖥️  If using SSH, connect with: ssh -X username@hostname"
    echo "2. 🖼️  Install virtual display: sudo apt-get install xvfb"
    echo "3. 🚀 Run with virtual display: xvfb-run -a python main.py"
    echo "4. 🏠 Use a system with GUI (desktop Linux, Windows, macOS)"
else
    echo "✅ Your system should support visible browser windows!"
fi

echo ""
echo "📍 WHERE THE BROWSER APPEARS:"
echo "============================"
echo "When properly configured, the browser will appear as:"
echo "• 🪟 A visible Chrome/Chromium window on your screen"
echo "• 📱 You can interact with it like any normal browser"
echo "• 👀 You'll see the AI performing actions in real-time"
echo "• 🎮 The window stays open between tasks for efficiency"