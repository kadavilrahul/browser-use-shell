from browser_use import Agent
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
from config import LLMConfig

MODEL_INFO = {
    "mixtral": {
        "provider": "Groq",
        "pricing": "Free (Limited time)",
        "display_name": "Mixtral-8x7B"
    },
    "claude-2.1": {
        "provider": "Anthropic",
        "pricing": "Paid",
        "display_name": "Claude 2.1"
    },
    "gemini-flash": {
        "provider": "Google",
        "pricing": "Free",
        "display_name": "Gemini 2.0 Flash"
    },
    "mistral-7b": {
        "provider": "OpenRouter",
        "pricing": "Paid",
        "display_name": "Mistral 7B"
    },
    "deepseek": {
        "provider": "DeepSeek",
        "pricing": "Paid",
        "display_name": "DeepSeek Chat"
    }
}

def display_models():
    """Display available models with serial numbers and provider information"""
    models = LLMConfig.get_available_models()
    print("\nAvailable Models:")
    print("================")
    
    all_models = [*models["paid"].items(), *models["free"].items()]
    count = 1
    
    for name, _ in all_models:
        info = MODEL_INFO[name]
        pricing_tag = "[Free]" if "Free" in info["pricing"] else "[Paid]"
        print(f"{count}. {info['provider']}: {info['display_name']} {pricing_tag}")
        count += 1
    
    return {i: name for i, name in enumerate([m[0] for m in all_models], 1)}

def get_user_input():
    """Get model selection and task from user"""
    model_map = display_models()
    
    while True:
        try:
            choice = int(input("\nSelect a model (enter the number): "))
            if choice in model_map:
                selected_model = model_map[choice]
                info = MODEL_INFO[selected_model]
                print(f"\nSelected: {info['provider']} {info['display_name']}")
                break
            print(f"Please enter a number between 1 and {len(model_map)}")
        except ValueError:
            print("Please enter a valid number")
    
    task = input("\nEnter your task (e.g., 'Go to Google and search for Python'): ")
    return selected_model, task

async def run_browser_task(task: str, model_name: str):
    """Run a browser automation task with specified model"""
    try:
        info = MODEL_INFO[model_name]
        print(f"\nRunning task with {info['provider']} {info['display_name']}...")
        models = LLMConfig.get_available_models()
        
        # Get model config
        if model_name in models["paid"]:
            model_config = models["paid"][model_name]
        elif model_name in models["free"]:
            model_config = models["free"][model_name]
        else:
            print(f"Model {model_name} not found in config")
            return False

        # Create appropriate LLM instance
        if "claude" in model_name:
            llm = ChatAnthropic(
                model=model_config["model"],
                anthropic_api_key=model_config["api_key"]
            )
        elif "gemini" in model_name:
            llm = ChatGoogleGenerativeAI(
                model=model_config["model"],
                google_api_key=model_config["api_key"]
            )
        elif "deepseek" in model_name:
            llm = ChatOpenAI(
                model=model_config["model"],
                api_key=model_config["api_key"],
                base_url=f"{model_config['base_url']}/v1"
            )
        elif "mistral" in model_name:
            llm = ChatOpenAI(
                model=model_config["model"],
                api_key=model_config["api_key"],
                base_url="https://openrouter.ai/api/v1"
            )
        else:  # Mixtral and others using OpenAI-compatible API
            llm = ChatOpenAI(
                model=model_config["model"],
                api_key=model_config["api_key"],
                base_url=model_config.get("endpoint", None)
            )

        # Create and run agent
        agent = Agent(task=task, llm=llm)
        result = await agent.run()
        return result

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    print("\nBrowser Automation with AI Models")
    print("================================")
    
    # Get user input for model and task
    model_name, task = get_user_input()
    
    # Run the task
    result = asyncio.run(run_browser_task(task, model_name))
    if result:
        print(f"\n✅ Task completed successfully")
    else:
        print(f"\n❌ Task failed")

if __name__ == "__main__":
    main()
