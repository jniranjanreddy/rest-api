az login --use-device-code --output none

az account show --query "{subscriptionId:id, tenantId:tenantId}" --output tsvcom