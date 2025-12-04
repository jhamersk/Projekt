# Infrastruktura Azure (IaC)

Katalog `infra/` zawiera definicję minimalnej infrastruktury Azure wymaganą w projekcie „Docker + DevOps + IaC (Azure)”. Infrastruktura jest przygotowana w technologii Bicep i składa się z dwóch plików: `main.bicep`, który tworzy grupę zasobów (Resource Group) i wywołuje moduł `resources.bicep`, oraz samego modułu, który tworzy Azure Container Registry (ACR) oraz Storage Account. Plik `parameters.json` zawiera wartości parametrów takie jak nazwa grupy zasobów, lokalizacja, nazwa ACR i nazwa Storage Account.

Poniżej znajduje się działanie komendy:

```
az deployment sub what-if \
    --location westeurope \
    --template-file main.bicep \
    --parameters parameters.json
```

![Screen z działania komendy](../docs/Screen.png)
