
import os
from dotenv import load_dotenv

from azure.identity import ClientSecretCredential
from azure.ai.projects import AIProjectClient

from agent_runner import run_agent

load_dotenv()

PROJECT_ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
AGENT_NAME = os.environ["FOUNDRY_AGENT_NAME"]

credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"]
)

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=credential
)

openai_client = project.get_openai_client(
    agent_name=AGENT_NAME
)
conversation = openai_client.conversations.create()
conversation_id = conversation.id
print("Conversation ID:", conversation_id)

print("\nAzure Cloud DevOps Agent is ready!")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ").strip()

    if question.lower() in ["exit", "quit"]:
        break

    try:
        answer = run_agent(
            openai_client,
            question,
    conversation_id
        )

        print("\nAgent:", answer, "\n")

    except Exception as error:
        print("Error:", error)

project.close()
