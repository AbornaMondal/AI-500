
import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure_tools import azure_tools

# Load environment variables
load_dotenv()

# Azure Service Principal authentication
credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"]
)

# Foundry configuration
endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
model_name = os.environ["FOUNDRY_MODEL_NAME"]
agent_name = os.environ["FOUNDRY_AGENT_NAME"]

# Connect to Azure AI Foundry project
project = AIProjectClient(
    endpoint=endpoint,
    credential=credential
)

# Create agent version
agent = project.agents.create_version(
    agent_name=agent_name,
    definition=PromptAgentDefinition(
        model=model_name,
        instructions="""
        You are an Azure Cloud and DevOps assistant.

        You can inspect Azure resources using Python functions.

        Available capabilities:
        1. List resource groups.
        2. List Azure resources.
        3. List virtual machines.

        Rules:
        - Use tools when the user asks about actual Azure resources.
        - Never invent resource information.
        - Always report actual tool results.
        - You have read-only access.
        - Never attempt resource creation, deletion,
          modification, or restart operations.
        """,
        tools=azure_tools
    )
)

print("Agent created successfully!")
print("Agent Name:", agent.name)
print("Agent Version:", agent.version)

project.close()
