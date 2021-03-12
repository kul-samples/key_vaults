from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVault = "kul-kv"
keyVaultUri = f"https://{keyVault}.vault.azure.net"
secretName = "postgresDbPwd"

credential = DefaultAzureCredential()
Secret_Client = SecretClient(vault_url=keyVaultUri, credential=credential)
retrievedSecret = Secret_Client.get_secret(secretName)

print(f"Value for the Secret '{secretName}' is: '{retrievedSecret.value}'")
