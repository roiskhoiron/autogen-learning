import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Load environment variables
load_dotenv()

def get_model_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    
    return OpenAIChatCompletionClient(
        model="Torcons",
        api_key=api_key,
        base_url="https://chat.torcons.ai/api/",
        model_info={
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "family": "unknown",
        }
    )
