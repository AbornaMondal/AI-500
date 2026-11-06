
import os

from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient

load_dotenv()
# Configuration
SUBSCRIPTION_ID = os.environ["AZURE_SUBSCRIPTION_ID"]

# Azure authentication
credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"]
)

# Azure management clients
resource_client = ResourceManagementClient(
    credential,
    SUBSCRIPTION_ID
)

compute_client = ComputeManagementClient(
    credential,
    SUBSCRIPTION_ID
)


# 1. List resource groups
def list_resource_groups():
    """Return all resource groups in the subscription."""

    groups = []

    for rg in resource_client.resource_groups.list():
        groups.append({
            "name": rg.name,
            "location": rg.location,
            "provisioning_state": rg.properties.provisioning_state
        })

    return groups


# 2. List Azure resources
def list_resources(
    resource_group_name=None,
    resource_type=None,
    location=None
):
    """Inspect resources, optionally filtering by RG, type or location."""

    if resource_group_name:
        resources = resource_client.resources.list_by_resource_group(
            resource_group_name
        )
    else:
        resources = resource_client.resources.list()

    results = []

    for resource in resources:

        if resource_type and resource.type.lower() != resource_type.lower():
            continue

        if location and resource.location.lower() != location.lower():
            continue

        results.append({
            "name": resource.name,
            "type": resource.type,
            "resource_group": resource.id.split("/")[4],
            "location": resource.location,
            "id": resource.id
        })

    return results


# 3. List virtual machines
def list_virtual_machines(resource_group_name=None):
    """Inspect Azure virtual machines."""

    if resource_group_name:
        vms = compute_client.virtual_machines.list(
            resource_group_name
        )
    else:
        vms = compute_client.virtual_machines.list_all()

    results = []

    for vm in vms:

        results.append({
            "name": vm.name,
            "location": vm.location,
            "vm_size": (
                vm.hardware_profile.vm_size
                if vm.hardware_profile else None
            ),
            "resource_group": vm.id.split("/")[4],
            "provisioning_state": (
                vm.provisioning_state
            )
        })

    return results
