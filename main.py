import asyncio
import os
import signal
import sys
from browser_use import Agent, Browser
from langchain_google_genai import ChatGoogleGenerativeAI
from api_manager import APIManager

class BrowserManager:
    """Manages persistent browser sessions"""
    
    def __init__(self):
        self.browser_instance = None
        self.browser_context = None
        self.is_browser_ready = False
    
    async def initialize_browser(self):
        """Initialize browser if not already done"""
        if not self.browser_instance:
            print("🌐 Initializing browser...")
            try:
                # Create browser - force headless mode since no GUI available
                self.browser_instance = Browser()
                # Set headless to True since no display is available
                self.browser_instance.browser_profile.headless = True
                # Disable sandbox for root user (common in containers/servers)
                self.browser_instance.browser_profile.chromium_sandbox = False

                # Add Chrome arguments for running as root and better compatibility
                if not self.browser_instance.browser_profile.args:
                    self.browser_instance.browser_profile.args = []
                self.browser_instance.browser_profile.args.extend([
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-gpu-sandbox',
                    '--disable-software-rasterizer'
                ])

                # Also ensure we have a proper display
                if os.getenv('DISPLAY'):
                    print(f"📺 Display detected: {os.getenv('DISPLAY')}")
                else:
                    print("⚠️ No DISPLAY environment variable found - browser may not be visible")

                self.browser_context = await self.browser_instance.new_context()
                self.is_browser_ready = True
                print("✅ Browser initialized successfully")
                print("🌐 Browser window should now be visible on your screen")
            except Exception as e:
                print(f"❌ Failed to initialize browser: {str(e)}")
                self.is_browser_ready = False
                raise
        else:
            print("🌐 Using existing browser session...")
    
    async def cleanup(self):
        """Safely cleanup browser resources"""
        try:
            if self.browser_context:
                print("🧹 Closing browser context...")
                await self.browser_context.close()
                self.browser_context = None
            if self.browser_instance:
                print("🧹 Closing browser...")
                await self.browser_instance.close()
                self.browser_instance = None
            self.is_browser_ready = False
            print("✅ Browser cleanup completed")
        except Exception as e:
            print(f"⚠️ Warning during browser cleanup: {str(e)}")
    
    async def reset_browser(self):
        """Reset browser session (close and reinitialize)"""
        await self.cleanup()
        await self.initialize_browser()

# Global browser manager
browser_manager = BrowserManager()

async def test_api_key(api_key):
    """Test if the API key is valid"""
    try:
        llm = ChatGoogleGenerativeAI(
            model=APIManager.MODELS["1"]['model'],
            google_api_key=api_key
        )
        await llm.ainvoke(APIManager.MODELS["1"]['test_prompt'])
        return True
    except Exception as e:
        print(f"Error testing API key: {str(e)}")
        return False

async def prompt_for_api_key():
    """Prompt user to add an API key"""
    print("\nNo API key found. Please add your Google API key.")
    print("You can get one from: https://makersuite.google.com/app/apikey")
    
    while True:
        api_key = input("\nEnter your Google API key: ").strip()
        if not api_key:
            print("API key cannot be empty.")
            continue
        
        # Basic validation
        if not APIManager.validate_key_format(api_key):
            print("❌ Invalid API key format. Please check your key.")
            continue
            
        print("Testing API key...")
        try:
            llm = ChatGoogleGenerativeAI(
                model=APIManager.MODELS["1"]['model'],
                google_api_key=api_key
            )
            await llm.ainvoke("Test")
            
            # If test passes, save the key
            if APIManager.add_key("1", api_key):
                print("✅ API key added successfully")
                return True
            else:
                print("❌ Failed to save API key")
                return False
        except Exception as e:
            print(f"❌ API key test failed: {str(e)}")
            retry = input("Would you like to try again? (y/n): ").strip().lower()
            if retry != 'y':
                return False

async def manage_api_keys():
    """Manage API keys"""
    while True:
        print("\nAPI Key Management")
        print("==================")
        
        # Show current keys
        current_key = APIManager.get_key("1")
        if current_key:
            print(f"Current Google API Key: {current_key[:10]}...{current_key[-4:]}")
        else:
            print("No Google API Key found")
        
        print("\n1. Add/Update Google API Key")
        print("2. Test Current API Key")
        print("3. Remove API Key")
        print("4. Back to Main Menu")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            await prompt_for_api_key()
        elif choice == "2":
            if current_key:
                print("Testing current API key...")
                if await test_api_key(current_key):
                    print("✅ API key is working correctly")
                else:
                    print("❌ API key test failed")
            else:
                print("No API key to test")
        elif choice == "3":
            if APIManager.remove_key("1"):
                print("✅ API key removed successfully")
            else:
                print("❌ Failed to remove API key")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

async def run_browser_task(task):
    """Run a browser automation task with persistent browser session"""
    try:
        # Get API key
        api_key = APIManager.get_key("1")
        if not api_key:
            print("❌ No API key found. Please add one first.")
            return False
        
        print(f"🚀 Starting task: {task}")
        
        # Set environment variable for the memory system
        os.environ['GOOGLE_API_KEY'] = api_key
        
        # Initialize browser if needed
        await browser_manager.initialize_browser()
        
        if not browser_manager.is_browser_ready:
            print("❌ Browser is not ready. Please try again.")
            return False
            
        # Create LLM
        llm = ChatGoogleGenerativeAI(
            model=APIManager.MODELS["1"]['model'],
            google_api_key=api_key
        )
            
        # Create and run agent
        agent = Agent(
            task=task,
            llm=llm,
            browser_session=browser_manager.browser_instance,
            browser_context=browser_manager.browser_context
        )
        
        print("🤖 Agent created successfully. Starting task execution...")
        print("👀 Watch the browser window to see the AI in action!")
        
        # Run the task
        result = await agent.run()
        
        print("✅ Task completed successfully!")
        print(f"Result: {result}")
        
        # Keep browser open for potential next task
        print("\n🌐 Browser will remain open for next task...")
        print("💡 You can now see the browser window with the completed task")
        return True
        
    except Exception as e:
        print(f"❌ Error running task: {str(e)}")
        import traceback
        traceback.print_exc()
        
        # Ask user if they want to reset browser
        reset_choice = input("\nWould you like to reset the browser session? (y/n): ").strip().lower()
        if reset_choice == 'y':
            try:
                await browser_manager.reset_browser()
                print("✅ Browser session reset successfully")
            except Exception as reset_error:
                print(f"❌ Failed to reset browser: {reset_error}")
        
        return False

def setup_signal_handlers():
    """Setup signal handlers for graceful shutdown"""
    def signal_handler(signum, frame):
        print(f"\n\n⚠️ Received signal {signum}. Shutting down gracefully...")
        # The cleanup will be handled in the main function's finally block
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

async def main():
    """Main application loop"""
    setup_signal_handlers()
    
    print("🌐 Browser Automation with AI")
    print("==============================")
    print("📝 Note: Browser will stay open between tasks for better performance")
    print("👀 Browser window will be VISIBLE so you can watch the AI work!")
    print("💡 Tip: Use Ctrl+C to exit gracefully")
    
    # Check display environment
    if not os.getenv('DISPLAY'):
        print("\n⚠️ WARNING: No DISPLAY environment variable detected!")
        print("   The browser may not be visible. Make sure you're running this on a system with GUI.")
        print("   If you're using SSH, try: ssh -X username@hostname")
        
    try:
        while True:
            print("\nBrowser Automation Menu")
            print("=====================")
            print("1. Run Task")
            print("2. Manage API Keys")
            print("3. Reset Browser Session")
            print("4. Close Browser")
            print("5. Exit")
            
            choice = input("\nSelect an option (1-5): ").strip()
            
            if choice == "1":
                # Check if API key exists
                api_key = APIManager.get_key("1")
                if not api_key:
                    print("❌ No API key found. Please add one first.")
                    await manage_api_keys()
                    continue
                
                task = input("\nEnter your task (or 'back' to return to menu): ").strip()
                if task.lower() in ['back', 'exit', '']:
                    if task.lower() == 'exit':
                        break
                    continue
                
                if task:
                    await run_browser_task(task)
                else:
                    print("Task cannot be empty.")
                    
            elif choice == "2":
                await manage_api_keys()
                
            elif choice == "3":
                if browser_manager.is_browser_ready:
                    try:
                        await browser_manager.reset_browser()
                        print("✅ Browser session reset successfully")
                    except Exception as e:
                        print(f"❌ Failed to reset browser session: {e}")
                else:
                    print("No browser session is currently active.")
                
            elif choice == "4":
                if browser_manager.is_browser_ready:
                    await browser_manager.cleanup()
                else:
                    print("No browser session is currently open.")
                
            elif choice == "5":
                break
                
            else:
                print("Invalid option. Please try again.")
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Cleanup on exit
        if browser_manager.is_browser_ready:
            print("\n🧹 Cleaning up browser session...")
            await browser_manager.cleanup()
        
        print("👋 Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())