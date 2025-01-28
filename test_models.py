import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from api_manager import APIManager

async def test_gemini():
    """Test Gemini model with API key"""
    print("\nTesting Gemini API key...")
    
    # Get API key
    api_key = APIManager.get_key("1")
    if not api_key:
        print("❌ No API key found")
        return False
    
    try:
        # Initialize Gemini
        llm = ChatGoogleGenerativeAI(
            model=APIManager.MODELS["1"]['model'],
            google_api_key=api_key
        )
        
        # Test the model
        print("\nAsking model to introduce itself...")
        response = await llm.ainvoke("Introduce yourself in one sentence")
        print(f"\nModel response: {response.content}")
        print("\n✅ API key is valid")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    """Main entry point"""
    asyncio.run(test_gemini())

if __name__ == "__main__":
    main()
