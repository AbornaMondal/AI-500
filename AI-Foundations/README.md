# Azure AI Foundations – Tool-Enabled Azure DevOps Agent

An AI-powered Azure Cloud and DevOps assistant built using **Azure AI Foundry, Python, and Azure SDKs**.

The project demonstrates how to build an AI agent that can understand natural-language questions, invoke Python functions, and retrieve real-time information about Azure resources.

## Project Overview

The goal is to build an intelligent Azure assistant that can help cloud and DevOps engineers inspect and understand their Azure infrastructure using natural-language interactions.

Instead of manually executing multiple Azure CLI commands, users can ask questions such as:

- List all resource groups in my Azure subscription.
- Show all virtual machines.
- Which Azure resources are deployed in East US?
- List resources in a particular resource group.
- Show details of my Azure infrastructure.

The AI agent identifies the appropriate function, executes it through Python, retrieves information from Azure, and generates a human-readable response.

## Architecture

```text
                User
                  |
                  v
          run_cloud_agent.py
                  |
                  v
          Azure AI Foundry Agent
                  |
                  v
             agent_runner.py
                  |
                  v
              azure_tools.py
                  |
                  v
           azure_inspector.py
                  |
                  v
         Azure Management APIs
                  |
                  v
          Azure Subscription
                  |
                  v
          Tool Execution Results
                  |
                  v
             AI Response
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Azure AI Foundry | AI agent development |
| Azure OpenAI | Language model inference |
| Azure AI Projects SDK | Foundry project integration |
| Azure Identity | Azure authentication |
| Azure Resource Management SDK | Resource inspection |
| Azure Compute Management SDK | Virtual machine inspection |
| python-dotenv | Environment variable management |
| Git | Version control |

## Project Structure

```text
AI-Foundations/
│
├── azure_inspector.py
├── azure_tools.py
├── agent_runner.py
├── run_cloud_agent.py
├── test_azure_inspector.py
│
├── create-agent.py
├── list-agents.py
│
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

### Python Modules

**1. azure_inspector.py – Azure Inspection Layer**

Contains Python functions that interact with Azure Management APIs.

Current capabilities:

- List Azure resource groups.
- List Azure resources.
- List virtual machines.
- Filter resources by resource group, resource type, and location.

**2. azure_tools.py – Function Tool Definitions**

Defines the tools exposed to the AI agent.

Each tool includes:

- Function name.
- Description.
- Input parameters.
- JSON parameter schema.

This allows the AI model to identify which Python function should be invoked based on the user's question.

**3. agent_runner.py – Agent Orchestration Layer**

Handles communication between the AI model and Python functions.

Responsibilities:

- Process AI-generated function calls.
- Map function names to Python implementations.
- Execute the requested functions.
- Return tool execution results to the AI model.
- Generate the final natural-language response.

**4. run_cloud_agent.py – Application Entry Point**

Starts the interactive application.

Responsibilities:

- Load environment variables.
- Authenticate with Azure.
- Connect to the Azure AI Foundry project.
- Initialize the existing AI agent.
- Accept user questions and display responses.

## Getting Started

### Prerequisites

- Python 3.10 or later.
- Azure subscription.
- Azure CLI installed.
- Azure AI Foundry project.
- Existing Azure OpenAI model deployment.
- Microsoft Entra ID App Registration.
- Azure Reader role assigned to the application's service principal.

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>

cd AI-Foundations
```

### 2. Create a virtual environment

```bash
python -m venv .venv

source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

```env
# Azure AI Foundry
FOUNDRY_PROJECT_ENDPOINT=

# Azure Authentication
AZURE_TENANT_ID=
AZURE_CLIENT_ID=
AZURE_CLIENT_SECRET=

# Azure Subscription
AZURE_SUBSCRIPTION_ID=
```

Never commit `.env` or expose credentials in source code.

### 5. Configure Azure permissions

Create a Microsoft Entra ID App Registration and use its associated Service Principal for Azure authentication.

Assign the following Azure RBAC role:

**Role:** Reader

**Scope:** Subscription or the specific resource group being inspected.

This provides read-only access to Azure resource information.

### 6. Run Azure inspection tests

```bash
python test_azure_inspector.py
```

### 7. Start the AI agent

```bash
python run_cloud_agent.py
```

Example interaction:

```text
Azure Cloud DevOps Agent is ready!

You: List all resource groups

Agent: Your Azure subscription contains the following
resource groups:
1. dev-resource-group
2. production-resource-group
3. monitoring-resource-group
```

*Example response for illustration.*

## Security Architecture

Security is an important consideration in this project.

The implementation follows the principle of least privilege.

- Dedicated Microsoft Entra ID application identity.
- Azure RBAC Reader permissions.
- Service principal authentication.
- Environment-based secret management.
- No hardcoded credentials.
- No infrastructure modification functions.

The initial implementation focuses exclusively on read-only Azure operations.

## Development Roadmap

### Phase 1 – Azure AI Foundations
- Connect Python application to Azure AI Foundry.
- Configure model deployment.
- Create and interact with an AI agent.

### Phase 2 – Tool-Enabled Agent (Current)
- Implement Python functions for Azure inspection.
- Integrate function calling.
- Connect Azure SDKs.
- Implement read-only resource inspection.
- Configure least-privilege authentication.

### Phase 3 – Advanced Azure Inspection
- Virtual machine power-state inspection.
- App Service monitoring.
- Storage account inspection.
- AKS cluster inspection.
- Azure Monitor and Log Analytics integration.

### Phase 4 – Controlled Azure Operations
- Resource restart operations.
- Infrastructure scaling.
- Approval-based execution.
- Audit logging.
- Role-based access controls.

### Phase 5 – Production-Ready AI DevOps Agent
- Multi-agent architecture.
- Model Context Protocol (MCP).
- Terraform integration.
- CI/CD pipeline troubleshooting.
- Monitoring and observability.

## Learning Objectives

Through this project, I am exploring:

- Azure AI Foundry agent development.
- LLM function calling and tool orchestration.
- Python-based Azure automation.
- Azure SDK integration.
- Microsoft Entra ID authentication.
- Azure RBAC and least-privilege security.
- AI-powered cloud infrastructure inspection.

## Disclaimer

This is a learning and experimentation project.

The current implementation is designed for read-only Azure resource inspection. Production deployment requires additional security controls, credential management, input validation, monitoring, and operational safeguards.

---

**Built as part of my AI + Cloud + DevOps learning journey.**
