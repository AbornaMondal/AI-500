
from azure_inspector import (
    list_resource_groups,
    list_resources,
    list_virtual_machines
)

print("\n===== RESOURCE GROUPS =====")
print(list_resource_groups())

print("\n===== AZURE RESOURCES =====")
print(list_resources())

print("\n===== VIRTUAL MACHINES =====")
print(list_virtual_machines())
