import asyncio
import sys
import os

# Ensure the root of autogen-project is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.coder_agent import create_coder_agent
from agents.reviewer_agent import create_reviewer_agent
from tasks.coding_task import get_coding_task
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console

async def main():
    coder = create_coder_agent()
    reviewer = create_reviewer_agent()
    
    task = get_coding_task()
    
    # Simple team: Coder and Reviewer working together
    team = RoundRobinGroupChat([coder, reviewer], max_turns=5)
    
    print(f"--- Starting Coding Task: {task} ---")
    await Console(team.run_stream(task=task))

if __name__ == "__main__":
    asyncio.run(main())
