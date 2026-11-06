from dotenv import load_dotenv
import os
from azure.identity import ClientSecretCredential

load_dotenv(".env", override=True)

tenant = os.environ["AZURE_TENANT_ID"]
client = os.environ["AZURE_CLIENT_ID"]
secret = os.environ["AZURE_CLIENT_SECRET"]

print("Tenant:", tenant)
print("Client:", client)
print("Secret loaded:", bool(secret))

credential = ClientSecretCredential(
    tenant_id=tenant,
    client_id=client,
    client_secret=secret
)

print("Credential client ID:", credential._client_id)

token = credential.get_token(
    "https://management.azure.com/.default"
)

print("Authentication successful!")