from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from msgraph.core import GraphClient

credential = DefaultAzureCredential()

subscription_id = "a467f55b-ddb4-4527-8100-f1f11e051f4a"
resource_group = "DemoEntraAgentID"

print("Authenticating using workload identity...")

resource_client = ResourceManagementClient(credential, subscription_id)
resource_client.resource_groups.update(
    resource_group,
    {"tags": {"WorkloadIdentityDemo": "Success"}}
)

print(f"Tag gezet op resource group: {resource_group}")

graph_client = GraphClient(credential=credential)
users = graph_client.get('/users?$select=displayName')
user_list = [u['displayName'] for u in users.json()['value']]

print("\nGebruikers in jouw tenant:")
for name in user_list:
    print(" -", name)

print("\nDemo voltooid — workload identity werkt!")
