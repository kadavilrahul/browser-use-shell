from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from config import LLMConfig
import asyncio

async def test_model(model_name: str, model_config: dict):
    """Test a specific model's API connection"""
    print(f"\nTesting {model_name}...")
    try:
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

        # Test the model
        response = await llm.ainvoke("Hello, are you working?")
        print(f"Response: {response.content}")
        return True
    except Exception as e:
        print(f"Error testing {model_name}: {str(e)}")
        return False

async def main():
    """Test all configured models"""
    models = LLMConfig.get_available_models()
    test_results = {}
    
    # Test each available model
    for category in ["paid", "free"]:
        for model_name, model_config in models[category].items():
            if model_config["api_key"]:  # Check if API key is valid
                success = await test_model(model_name, model_config)
                test_results[model_name] = success
            else:
                print(f"Skipping {model_name} due to invalid API key")
                test_results[model_name] = False

    # Print test results summary
    print("\nTest Results Summary:")
    print("--------------------")
    for model_name, success in test_results.items():
        status = "✅ Working" if success else "❌ Failed"
        print(f"{model_name}: {status}")

if __name__ == "__main__":
    asyncio.run(main())
