param location string
param acrName string
param storageAccountName string

resource acr 'Microsoft.ContainerRegistry/registries@2025-11-01' = {
  name: acrName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}

resource storage 'Microsoft.Storage/storageAccounts@2025-06-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Cold'
  }
}

output acrId string = acr.id
output acrLoginServer string = acr.properties.loginServer
output storageAccountId string = storage.id
output storageAccountPrimaryEndpoint string = storage.properties.primaryEndpoints.blob
