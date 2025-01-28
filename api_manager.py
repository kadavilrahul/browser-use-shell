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
            "model": "gemini-2.0-flash-exp",
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
        os.makedirs(os.path.dirname(cls.KEY_FILE), exist_ok=True)
        if not os.path.exists(cls.KEY_FILE):
            with open(cls.KEY_FILE, "w") as f:
                json.dump({}, f)
    
    @classmethod
    def _load_keys(cls) -> Dict[str, str]:
        """Load API key from file"""
        cls._ensure_key_file()
        try:
            with open(cls.KEY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    
    @classmethod
    def _save_keys(cls, keys: Dict[str, str]) -> None:
        """Save API key to file"""
        cls._ensure_key_file()
        with open(cls.KEY_FILE, "w") as f:
            json.dump(keys, f)
    
    @classmethod
    def add_key(cls, model_num: str, api_key: str) -> bool:
        """Add Gemini API key"""
        if model_num != "1" or not api_key:
            return False
            
        keys = cls._load_keys()
        keys[model_num] = api_key
        try:
            cls._save_keys(keys)
            return True
        except Exception:
            return False
    
    @classmethod
    def remove_key(cls, model_num: str) -> bool:
        """Remove Gemini API key"""
        if model_num != "1":
            return False
            
        keys = cls._load_keys()
        if model_num in keys:
            del keys[model_num]
            try:
                cls._save_keys(keys)
                return True
            except Exception:
                return False
        return False
    
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
        key = keys.get(model_num, "").strip()
        return key if key else None
    
    @classmethod
    def list_models(cls) -> None:
        """List Gemini model with status"""
        print("\nAvailable Model:")
        print("===============")
        
        model = cls.MODELS["1"]
        key = cls.get_key("1")
        status = "✅" if key else "❌"
        print(f"1. {model['name']} - {model['provider']} ({model['pricing']}) {status}")
