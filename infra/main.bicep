targetScope = 'subscription'

param resourceGroupName string
param location string
param acrName string
param storageAccountName string

resource rg 'Microsoft.Resources/resourceGroups@2025-04-01' = {
  name: resourceGroupName
  location: location
}

output resourceGroupName string = rg.name
output resourceGroupId string = rg.id

module resourcesModule './resources.bicep' = {
  name: 'deployResources'
  scope: rg
  params: {
    acrName: acrName
    storageAccountName: storageAccountName
    location: location
  }
}

output acrId string = resourcesModule.outputs.acrId
output acrLoginServer string = resourcesModule.outputs.acrLoginServer
output storageAccountId string = resourcesModule.outputs.storageAccountId
output storageAccountPrimaryEndpoint string = resourcesModule.outputs.storageAccountPrimaryEndpoint
