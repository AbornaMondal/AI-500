
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

load_dotenv()

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project.agents.create_version(
    agent_name="dona-devops-agent",
    definition=PromptAgentDefinition(
        model=os.environ["FOUNDRY_MODEL_NAME"],
        instructions="""
        You are an advanced Azure AI and DevOps assistant.

        Your expertise includes:
        - Azure infrastructure
        - Terraform and Infrastructure as Code
        - Kubernetes and AKS
        - Azure DevOps and Jenkins
        - AI and Machine Learning
        - Azure AI Foundry and AI Agents

        Provide practical examples and production-ready
        recommendations.
        """
    )
)

print("New agent version created!")
print("Agent name:", agent.name)
print("Agent version:", agent.version)
