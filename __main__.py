"""An Azure Python Pulumi program"""

import pulumi
from pulumi_azure import core, storage

# Create an Azure Resource Group
resource_group = core.ResourceGroup('net-eng')

# Create an Azure resource (Storage Account)
account = storage.Account('netsta',
                          # The location for the storage account will be derived automatically from the resource group.
                          resource_group_name=resource_group.name,
                          account_tier='Standard',
                          account_replication_type='LRS',
                          tags={"Environment": "Dev"})

# Export the connection string for the storage account
pulumi.export('connection_string', account.primary_connection_string)
