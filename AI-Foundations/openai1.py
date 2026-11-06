import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Load environment variables
load_dotenv()

endpoint = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
model_name = os.getenv("FOUNDRY_MODEL_NAME")

# Authenticate using Azure CLI credentials
credential = DefaultAzureCredential()

# Connect to Azure AI Foundry
project = AIProjectClient(
    endpoint=endpoint,
    credential=credential
)

# Get OpenAI-compatible client
openai_client = project.get_openai_client()

# Send prompt to deployed model
response = openai_client.responses.create(
    model=model_name,
    input="Explain Azure DevOps in simple terms."
)

# Print model response
print("\nAzure OpenAI Response:")
print(response.output_text)

# Close connections
openai_client.close()
project.close()
credential.close()