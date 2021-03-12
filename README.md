# azure_access_key_vault_python_from_vm
## Setup Environment

### Assign Identity to VM
```
$ az vm identity assign --name "<vm-name>" --resource-group "<resource-group-name>"
{- Finished ..
  "systemAssignedIdentity": "82b260be-ce93-477f-8a1a-d0819c0d6700",
  "userAssignedIdentities": {}
}
```
### Setting up Access policy for VM in keyvault
```
$ az keyvault set-policy --name "kul-kv" --object-id "<systemAssignedIdentity_from_above_command" --secret-permissions get list
{- Finished ..
  "id": "/subscriptions/312b69f3-480b-46a3-afd6-ae7c053ab0ae/resourceGroups/kul-synechron/providers/Microsoft.KeyVault/vaults/kul-kv",
  "location": "eastus",
  "name": "kul-kv",
  "properties": {
    "accessPolicies": [
      {
        "applicationId": null,
        "objectId": "3e11761d-31e5-4226-a0d2-d5970116e953",
        "permissions": {
          "certificates": [
            "Get",
            "List",
            "Update",
            "Create",
            "Import",
            "Delete",
            "Recover",
            "Backup",
            "Restore",
            "ManageContacts",
            "ManageIssuers",
            "GetIssuers",
            "ListIssuers",
            "SetIssuers",
            "DeleteIssuers"
          ],
          "keys": [
            "Get",
            "List",
            "Update",
            "Create",
            "Import",
            "Delete",
            "Recover",
            "Backup",
            "Restore"
          ],
          "secrets": [
            "Get",
            "List",
            "Set",
            "Delete",
            "Recover",
            "Backup",
            "Restore"
          ],
          "storage": null
        },
        "tenantId": "af1b6ff7-ddf1-4bd1-acf5-5b432a4c65c0"
      },
      {
        "applicationId": null,
        "objectId": "82b260be-ce93-477f-8a1a-d0819c0d6700",
        "permissions": {
          "certificates": null,
          "keys": null,
          "secrets": [
            "get",
            "list"
          ],
          "storage": null
        },
        "tenantId": "af1b6ff7-ddf1-4bd1-acf5-5b432a4c65c0"
      }
    ],
    "createMode": null,
    "enablePurgeProtection": null,
    "enableRbacAuthorization": false,
    "enableSoftDelete": true,
    "enabledForDeployment": true,
    "enabledForDiskEncryption": true,
    "enabledForTemplateDeployment": true,
    "networkAcls": null,
    "privateEndpointConnections": null,
    "provisioningState": "Succeeded",
    "sku": {
      "family": "A",
      "name": "Standard"
    },
    "softDeleteRetentionInDays": 7,
    "tenantId": "af1b6ff7-ddf1-4bd1-acf5-5b432a4c65c0",
    "vaultUri": "https://kul-kv.vault.azure.net/"
  },
  "resourceGroup": "kul-synechron",
  "tags": {
    "Day": "3"
  },
  "type": "Microsoft.KeyVault/vaults"
}
```
### Settng up python3, pip3 & python libraries
```
$ sudo apt-get update -y
$ sudo apt-get install -y python3
$ sudo apt-get install -y python3-pip
$ sudo -H pip3 install --upgrade pip
$ pip3 install azure-keyvault-secrets
$ pip3 install azure.identity
```
### Running Application to Retreive Secret
```
$ python3 retrieved_secret.py
```
