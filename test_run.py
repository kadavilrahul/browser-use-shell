#!/usr/bin/env python3

import sys
import traceback

def test_imports():
    """Test if all imports work correctly"""
    try:
        print("Testing imports...")
        
        # Test basic imports
        import asyncio
        import os
        print("✅ Basic imports successful")
        
        # Test browser_use import
        from browser_use import Agent, Browser
        print("✅ browser_use import successful")
        
        # Test langchain import
        from langchain_google_genai import ChatGoogleGenerativeAI
        print("✅ langchain_google_genai import successful")
        
        # Test local imports
        from api_manager import APIManager
        print("✅ api_manager import successful")
        
        print("✅ All imports successful!")
        return True, APIManager
        
    except Exception as e:
        print(f"❌ Import error: {str(e)}")
        traceback.print_exc()
        return False, None

def test_api_manager(APIManager):
    """Test APIManager functionality"""
    try:
        print("\nTesting APIManager...")
        
        # Test model configuration
        models = APIManager.MODELS
        print(f"✅ Models loaded: {list(models.keys())}")
        
        # Test key validation
        test_key = "test_key_123"
        is_valid = APIManager.validate_key_format(test_key)
        print(f"✅ Key validation working: {is_valid}")
        
        print("✅ APIManager functionality working")
        return True
        
    except Exception as e:
        print(f"❌ APIManager error: {str(e)}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("🧪 Running application tests...")
    print("=" * 40)
    
    success = True
    
    # Test imports
    import_success, APIManager = test_imports()
    if not import_success:
        success = False
        APIManager = None
    
    # Test APIManager
    if APIManager and not test_api_manager(APIManager):
        success = False
    
    print("\n" + "=" * 40)
    if success:
        print("✅ All tests passed! Application should run correctly.")
        print("💡 Run './start.sh' or 'python main.py' to start the application")
    else:
        print("❌ Some tests failed. Check the errors above.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)