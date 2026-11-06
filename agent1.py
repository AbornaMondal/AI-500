
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure_tools import azure_tools


load_dotenv()

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
model_name = os.environ["FOUNDRY_MODEL_NAME"]
agent_name = os.environ["FOUNDRY_AGENT_NAME"]
project = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential()
)

# Create an agent in Azure AI Foundry
agent = project.agents.create_version(
    agent_name=agent_name,
    definition=PromptAgentDefinition(
        model=model_name,
        instructions="""
        You are a Cloud and DevOps AI Assistant.

        Your expertise includes:
        - Microsoft Azure
        - Terraform
        - Kubernetes and AKS
        - Azure DevOps CI/CD
        - Cloud troubleshooting

        Explain technical concepts clearly.
        Provide code examples when useful.
        Never invent Azure resource states.
        also add some important points for clearing interviews 
        """
    )
)

print(f"Agent created: {agent.name}")
print(f"Agent version: {agent.version}")

# Connect to the agent
openai_client = project.get_openai_client(
    agent_name=agent_name
)

# Start a conversation
conversation = openai_client.conversations.create()

print("\nCloud DevOps Agent is ready!")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        continue

    try:
        response = openai_client.responses.create(
            conversation=conversation.id,
            input=question
        )
        print("\nAgent:", response.output_text, "\n")

    except Exception as error:
        print("Error:", error)
