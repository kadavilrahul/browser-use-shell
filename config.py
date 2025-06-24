import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def validate_api_key(key_name: str, key_value: str | None, required: bool = False) -> str | None:
    """Validate API key format and presence"""
    if not key_value:
        if required:
            raise ValueError(f"Missing {key_name} in .env file.")
        return None
    
    # Check for common placeholder patterns
    placeholder_patterns = ["your_", "sk_", "key_"]
    if any(key_value.startswith(pattern) for pattern in placeholder_patterns):
        if required:
            raise ValueError(f"Please replace the placeholder {key_name} with your actual API key.")
        return None
    
    return key_value

class LLMConfig:
    """Configuration for Gemini Language Model"""
    
    # Google Gemini Flash configuration
    GEMINI = {
        "model": "gemini-2.0-flash-exp",
        "api_key": validate_api_key("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
    }
    
    @classmethod
    def get_available_models(cls) -> Dict[str, Dict[str, Any]]:
        """Get models with valid API keys"""
        models = {}
        
        # Add Gemini if API key is valid
        if cls.GEMINI["api_key"]:
            models["gemini-flash"] = cls.GEMINI
            
        # Ensure model is available
        if not models:
            raise ValueError("Gemini API key is required. Please provide your Google API key.")
            
        return models

    @classmethod
    def validate_model_name(cls, model_name: str) -> bool:
        """Check if a model name is valid"""
        models = cls.get_available_models()
        return model_name in models

    @classmethod
    def get_model_config(cls, model_name: str) -> Dict[str, Any]:
        """Get configuration for a specific model"""
        models = cls.get_available_models()
        
        if model_name in models:
            return models[model_name]
        else:
            raise ValueError(f"Invalid model name: {model_name}. Only 'gemini-flash' is supported.")
