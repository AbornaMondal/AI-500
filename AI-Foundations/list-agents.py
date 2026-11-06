
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agents = project.agents.list()

for agent in agents:
    print("\n-------------------------")
    print("Agent Name:", agent.name)
    print("Agent ID:", agent.id)

    print("Versions:", agent.versions)

    if agent.versions:
        for version in agent.versions:
            print("Version:", version)
