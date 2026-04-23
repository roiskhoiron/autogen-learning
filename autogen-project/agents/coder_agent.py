from autogen_agentchat.agents import AssistantAgent
from config import get_model_client

def create_coder_agent():
    model_client = get_model_client()
    return AssistantAgent(
        name="Coder",
        model_client=model_client,
        system_message="You are an expert programmer. Your goal is to write high-quality, efficient, and well-documented code based on the given requirements."
    )
