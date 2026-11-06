
from azure.ai.projects.models import FunctionTool

azure_tools = [

    FunctionTool(
        name="list_resource_groups",
        description="List all Azure resource groups in the subscription.",
        parameters={
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        },
        strict=True
    ),

    FunctionTool(
        name="list_resources",
        description=(
            "List Azure resources. Optionally filter by "
            "resource group, resource type or Azure location."
        ),
        parameters={
            "type": "object",
            "properties": {
                "resource_group_name": {
                    "type": ["string", "null"],
                    "description": "Resource group name or null."
                },
                "resource_type": {
                    "type": ["string", "null"],
                    "description": "Azure resource type or null."
                },
                "location": {
                    "type": ["string", "null"],
                    "description": "Azure region or null."
                }
            },
            "required": [
                "resource_group_name",
                "resource_type",
                "location"
            ],
            "additionalProperties": False
        },
        strict=True
    ),

    FunctionTool(
        name="list_virtual_machines",
        description="List Azure virtual machines in the subscription.",
        parameters={
            "type": "object",
            "properties": {
                "resource_group_name": {
                    "type": ["string", "null"],
                    "description": "Resource group name or null."
                }
            },
            "required": ["resource_group_name"],
            "additionalProperties": False
        },
        strict=True
    )
]
