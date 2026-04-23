from autogen_agentchat.agents import AssistantAgent
from config import get_model_client

def create_reviewer_agent():
    model_client = get_model_client()
    return AssistantAgent(
        name="Reviewer",
        model_client=model_client,
        system_message="You are a senior code reviewer. Your goal is to review code for bugs, security issues, and adherence to best practices. Provide constructive feedback."
    )
