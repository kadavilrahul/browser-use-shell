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
    """Configuration for Language Models"""
    
    class PaidModels:
        """Paid model configurations"""
        
        # Groq (Mixtral)
        MIXTRAL = {
            "model": "mixtral-8x7b-32768",
            "endpoint": "https://api.groq.com/openai/v1",
            "api_key": validate_api_key("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))
        }
        
        # Anthropic Claude
        CLAUDE = {
            "model": "claude-2.1",
            "api_key": validate_api_key("ANTHROPIC_API_KEY", os.getenv("ANTHROPIC_API_KEY"))
        }
        
        # Google Gemini Flash
        GEMINI = {
            "model": "models/gemini-2.0-flash-exp",
            "api_key": validate_api_key("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))
        }
        
    class FreeModels:
        """Free model configurations"""
        
        # OpenRouter Mistral
        MISTRAL = {
            "model": "mistral-7b-instruct",
            "api_key": validate_api_key("OPENROUTER_API_KEY", os.getenv("OPENROUTER_API_KEY")),
            "base_url": "https://openrouter.ai/api/v1"
        }
        
        # DeepSeek
        DEEPSEEK = {
            "model": "deepseek-chat",
            "api_key": validate_api_key("DEEPSEEK_API_KEY", os.getenv("DEEPSEEK_API_KEY")),
            "base_url": "https://api.deepseek.com"
        }
    
    @classmethod
    def get_available_models(cls) -> Dict[str, Dict[str, Any]]:
        """Get models with valid API keys"""
        models = {"paid": {}, "free": {}}
        
        # Add models with valid API keys
        if cls.PaidModels.MIXTRAL["api_key"]:
            models["paid"]["mixtral"] = cls.PaidModels.MIXTRAL
        if cls.PaidModels.CLAUDE["api_key"]:
            models["paid"]["claude-2.1"] = cls.PaidModels.CLAUDE
        if cls.PaidModels.GEMINI["api_key"]:
            models["paid"]["gemini-flash"] = cls.PaidModels.GEMINI
        if cls.FreeModels.MISTRAL["api_key"]:
            models["free"]["mistral-7b"] = cls.FreeModels.MISTRAL
        if cls.FreeModels.DEEPSEEK["api_key"]:
            models["free"]["deepseek"] = cls.FreeModels.DEEPSEEK
            
        # Ensure at least one model is available
        if not any(models.values()):
            raise ValueError("At least one API key is required. Please provide an API key for any of the supported models.")
            
        return models

    @classmethod
    def validate_model_name(cls, model_name: str) -> bool:
        """Check if a model name is valid"""
        models = cls.get_available_models()
        return (
            model_name in models["paid"] or 
            model_name in models["free"]
        )

    @classmethod
    def get_model_config(cls, model_name: str) -> Dict[str, Any]:
        """Get configuration for a specific model"""
        models = cls.get_available_models()
        
        if model_name in models["paid"]:
            return models["paid"][model_name]
        elif model_name in models["free"]:
            return models["free"][model_name]
        else:
            raise ValueError(
                f"Invalid model name: {model_name}. Available models: "
                f"{list(models['paid'].keys()) + list(models['free'].keys())}"
            )
