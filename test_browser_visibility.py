#!/usr/bin/env python3
"""
Test script to verify browser visibility
This script will open a browser window to test if it's visible
"""

import asyncio
import os
from browser_use import Browser

async def test_browser_visibility():
    """Test if browser opens in visible mode"""
    print("🧪 Testing Browser Visibility")
    print("=" * 30)
    
    # Check display environment
    display = os.getenv('DISPLAY')
    if display:
        print(f"✅ Display environment: {display}")
    else:
        print("⚠️ No DISPLAY environment variable found")
        print("   Browser may not be visible")
    
    print("\n🌐 Creating browser instance...")
    
    try:
        # Create browser with explicit headless=False and sandbox disabled for root
        browser = Browser()
        browser.browser_profile.headless = False
        browser.browser_profile.chromium_sandbox = False  # Disable sandbox for root
        
        # Add additional Chrome arguments for running as root
        if hasattr(browser.browser_profile, 'args'):
            if not browser.browser_profile.args:
                browser.browser_profile.args = []
            browser.browser_profile.args.extend([
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu-sandbox',
                '--disable-software-rasterizer'
            ])
        
        print("🚀 Starting browser...")
        context = await browser.new_context()
        
        print("✅ Browser started successfully!")
        print("👀 You should now see a browser window on your screen")
        
        # Navigate to a test page
        print("\n🔗 Navigating to Google...")
        await browser.navigate("https://www.google.com")
        
        print("✅ Navigation completed!")
        print("📺 The browser window should now show Google homepage")
        
        # Wait for user confirmation
        input("\n⏳ Press Enter after you can see the browser window...")
        
        # Take a screenshot to verify
        print("📸 Taking screenshot...")
        screenshot_path = "browser_test_screenshot.png"
        await browser.take_screenshot(screenshot_path)
        print(f"✅ Screenshot saved as: {screenshot_path}")
        
        # Cleanup
        print("\n🧹 Cleaning up...")
        await context.close()
        await browser.close()
        print("✅ Test completed successfully!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during browser test: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_browser_visibility())
    if success:
        print("\n🎉 Browser visibility test PASSED!")
        print("   The browser should be visible when running tasks.")
    else:
        print("\n❌ Browser visibility test FAILED!")
        print("   Check the error messages above.")