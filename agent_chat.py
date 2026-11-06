
import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from azure.ai.projects import AIProjectClient

load_dotenv()


class AgentChat:

    def __init__(self):

        self.credential = ClientSecretCredential(
            tenant_id=os.environ["AZURE_TENANT_ID"],
            client_id=os.environ["AZURE_CLIENT_ID"],
            client_secret=os.environ["AZURE_CLIENT_SECRET"]
        )

        self.project = AIProjectClient(
            endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
            credential=self.credential
        )

        self.agent_name = os.environ["FOUNDRY_AGENT_NAME2"]

        # Connect to existing Foundry agent
        self.openai = self.project.get_openai_client(
            agent_name=self.agent_name
        )

        self.conversation = None
        self.conversation_id = None

    # Create a new conversation
    def create_conversation(self):

        self.conversation = self.openai.conversations.create()
        self.conversation_id = self.conversation.id

        print("Conversation created!")
        print("Conversation ID:", self.conversation_id)

        return self.conversation_id

    # Resume an existing conversation
    def resume_conversation(self, conversation_id):

        self.conversation_id = conversation_id

        print("Resumed conversation:", self.conversation_id)

    # Send a message
    def send_message(self, message):

        if not self.conversation_id:
            raise ValueError("Create or resume a conversation first.")

        response = self.openai.responses.create(
            conversation=self.conversation_id,
            input=message
        )

        print("\nAgent:", response.output_text)

        return response

    # Close clients
    def close(self):

        self.openai.close()
        self.project.close()


if __name__ == "__main__":

    chat = AgentChat()

    try:
        chat.create_conversation()

        while True:

            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                break

            response = chat.send_message(user_input)

    finally:
        chat.close()
