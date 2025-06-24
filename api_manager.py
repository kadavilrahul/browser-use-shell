import os
import json
from pathlib import Path
from typing import Dict, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class APIManager:
    """Manages API key for Gemini model"""
    
    # File to store API key
    KEY_FILE = os.path.join(str(Path.home()), ".browser_use", "api_keys.json")
    
    # Gemini model configuration
    MODELS = {
        "1": {
            "model": "gemini-2.0-flash-exp",  # Updated model name
            "name": "Gemini 2.0 Flash",
            "provider": "Google",
            "key_name": "GOOGLE_API_KEY",
            "pricing": "Free",
            "test_prompt": "Say 'Hello' if you can hear me."
        }
    }
    
    @classmethod
    def _ensure_key_file(cls) -> None:
        """Ensure the key file directory exists"""
        try:
            os.makedirs(os.path.dirname(cls.KEY_FILE), exist_ok=True)
            if not os.path.exists(cls.KEY_FILE):
                with open(cls.KEY_FILE, "w") as f:
                    json.dump({}, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not create key file directory: {e}")
    
    @classmethod
    def _load_keys(cls) -> Dict[str, str]:
        """Load API key from file"""
        cls._ensure_key_file()
        try:
            with open(cls.KEY_FILE, "r") as f:
                data = json.load(f)
                return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, FileNotFoundError, Exception) as e:
            print(f"Warning: Could not load API keys: {e}")
            return {}
    
    @classmethod
    def _save_keys(cls, keys: Dict[str, str]) -> bool:
        """Save API key to file"""
        try:
            cls._ensure_key_file()
            with open(cls.KEY_FILE, "w") as f:
                json.dump(keys, f, indent=2)
            return True
        except Exception as e:
            print(f"Error: Could not save API keys: {e}")
            return False

    @classmethod
    def add_key(cls, model_num: str, api_key: str) -> bool:
        """Add Gemini API key"""
        if model_num != "1" or not api_key or not api_key.strip():
            return False
            
        keys = cls._load_keys()
        keys[model_num] = api_key.strip()
        return cls._save_keys(keys)
    
    @classmethod
    def remove_key(cls, model_num: str) -> bool:
        """Remove Gemini API key"""
        if model_num != "1":
            return False
            
        keys = cls._load_keys()
        if model_num in keys:
            del keys[model_num]
            return cls._save_keys(keys)
        return True  # Return True if key doesn't exist (already removed)
    
    @classmethod
    def get_key(cls, model_num: str) -> Optional[str]:
        """Get Gemini API key"""
        if model_num != "1":
            return None
            
        # First check environment variable
        env_key = os.getenv(cls.MODELS[model_num]["key_name"])
        if env_key and env_key.strip():
            return env_key.strip()
            
        # Then check key file
        keys = cls._load_keys()
        key = keys.get(model_num, "")
        return key.strip() if key and key.strip() else None
    
    @classmethod
    def list_models(cls) -> None:
        """List Gemini model with status"""
        print("\nAvailable Model:")
        print("===============")
        
        model = cls.MODELS["1"]
        key = cls.get_key("1")
        status = "✅" if key else "❌"
        print(f"1. {model['name']} - {model['provider']} ({model['pricing']}) {status}")
    
    @classmethod
    def validate_key_format(cls, api_key: str) -> bool:
        """Basic validation of API key format"""
        if not api_key or not isinstance(api_key, str):
            return False
        
        api_key = api_key.strip()
        
        # Basic checks for Google API key format
        if len(api_key) < 20:  # Google API keys are typically longer
            return False
        
        # Check for common placeholder patterns
        placeholder_patterns = ["your_", "YOUR_", "replace_", "REPLACE_", "example"]
        if any(pattern in api_key for pattern in placeholder_patterns):
            return False
        
        return True