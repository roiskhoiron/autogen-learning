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
        model="gemini-2.0-flash",
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
