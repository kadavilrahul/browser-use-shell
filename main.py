from browser_use import Agent
from browser_use.browser import browser
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
from api_manager import APIManager

Browser = browser.Browser
BrowserContext = browser.BrowserContext

async def test_api_key():
    """Test if the Gemini API key works"""
    api_key = APIManager.get_key("1")
    if not api_key:
        print("No API key found for Gemini")
        return False
        
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
    api_key = input("Enter Gemini API key: ").strip()
    
    if not api_key:
        print("❌ API key cannot be empty")
        return False
        
    try:
        # Test the API key first
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
        print(f"❌ Invalid API key: {str(e)}")
        return False

async def manage_api_keys():
    """Manage API keys - add, remove, or list"""
    while True:
        print("\nAPI Key Management")
        print("=================")
        print("1. Add/Update API Key")
        print("2. Remove API Key")
        print("3. List Status")
        print("4. Return to Main Menu")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            await prompt_for_api_key()
        elif choice == "2":
            if APIManager.remove_key("1"):
                print("✅ API key removed")
            else:
                print("❌ No API key found")
        elif choice == "3":
            APIManager.list_models()
            input("\nPress Enter to continue...")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

async def run_task(task: str, browser_instance=None, browser_context=None):
    """Run a single browser task"""
    try:
        # Get API key
        api_key = APIManager.get_key("1")
        if not api_key:
            print("No API key found for Gemini")
            return browser_instance, browser_context
            
        # Create browser if needed
        if browser_instance is None:
            browser_instance = Browser()
            
        # Create context if needed    
        if browser_context is None:
            browser_context = await browser_instance.new_context()
            
        # Create LLM
        llm = ChatGoogleGenerativeAI(
            model=APIManager.MODELS["1"]['model'],
            google_api_key=api_key
        )
            
        # Create and run agent
        agent = Agent(
            task=task,
            llm=llm,
            browser=browser_instance,
            browser_context=browser_context
        )
        await agent.run()
        
        return browser_instance, browser_context
            
    except Exception as e:
        print(f"Error: {str(e)}")
        # Clean up on error
        if browser_context:
            await browser_context.close()
        if browser_instance:
            await browser_instance.close()
        return None, None

async def run_tasks():
    """Run browser tasks"""
    browser_instance = None
    browser_context = None
    
    try:
        while True:
            # Check for API key
            if not APIManager.get_key("1"):
                if not await prompt_for_api_key():
                    return
            
            # First time menu
            if browser_instance is None:
                print("\nBrowser Automation Menu")
                print("=====================")
                print("1. Run Task")
                print("2. Manage API Keys")
                print("3. Exit")
                
                choice = input("\nSelect an option (1-3): ").strip()
                
                if choice == "2":
                    await manage_api_keys()
                    continue
                elif choice == "3":
                    break
                elif choice != "1":
                    print("Invalid choice")
                    continue
            
            # Get task input
            task = input("\nEnter your task (or 'exit' to quit): ").strip()
            if not task:
                print("Task cannot be empty")
                continue
            elif task.lower() == 'exit':
                break
                
            # Run the task
            browser_instance, browser_context = await run_task(
                task, 
                browser_instance, 
                browser_context
            )
            
            if browser_instance is None:
                # Error occurred, show menu again
                continue
                
    finally:
        # Clean up browser resources
        if browser_context:
            await browser_context.close()
        if browser_instance:
            await browser_instance.close()

async def main_async():
    """Main async function"""
    while True:
        try:
            await run_tasks()
            break
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            cont = input("\nRetry? (y/n): ").lower().strip()
            if cont != 'y':
                break

def main():
    """Main entry point"""
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
