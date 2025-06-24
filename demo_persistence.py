#!/usr/bin/env python3
"""
Demo script showing browser persistence functionality
This script demonstrates how the browser stays open between tasks
"""

import asyncio
import os
from browser_use import Browser
from langchain_google_genai import ChatGoogleGenerativeAI
from api_manager import APIManager

async def demo_browser_persistence():
    """Demonstrate browser staying open between operations"""
    print("🎯 Browser Persistence Demo")
    print("=" * 30)
    
    # Check if API key exists
    api_key = APIManager.get_key("1")
    if not api_key:
        print("❌ No API key found. Please run the main application first to add your API key.")
        print("   Run: python main.py")
        return
    
    print("✅ API key found")
    print("🌐 Initializing browser...")
    
    # Create browser instance
    browser = Browser()
    context = await browser.new_context()
    
    print("✅ Browser initialized and ready")
    print("📝 Browser will now stay open for multiple operations...")
    
    # Simulate multiple operations
    operations = [
        "Navigate to Google homepage",
        "Search for 'Python programming'",
        "Click on the first result"
    ]
    
    for i, operation in enumerate(operations, 1):
        print(f"\n🔄 Operation {i}: {operation}")
        print("   (In real usage, AI would execute this task)")
        
        # Simulate some work
        await asyncio.sleep(1)
        
        print(f"   ✅ Operation {i} completed")
        print("   🌐 Browser remains open and ready for next task")
    
    print(f"\n🎉 Demo completed!")
    print("📊 Browser session statistics:")
    print(f"   - Browser instance: {'Active' if browser else 'Inactive'}")
    print(f"   - Context: {'Active' if context else 'Inactive'}")
    print("   - Memory usage: Optimized (single session)")
    
    # Keep browser open for a moment
    print("\n⏳ Browser will stay open for 5 seconds to demonstrate persistence...")
    await asyncio.sleep(5)
    
    # Cleanup
    print("\n🧹 Cleaning up demo...")
    await context.close()
    await browser.close()
    print("✅ Demo cleanup completed")

if __name__ == "__main__":
    asyncio.run(demo_browser_persistence())