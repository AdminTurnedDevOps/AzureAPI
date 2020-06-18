# Run this command to generate Azure CLI credentials for authenticating with GitHub Actions

param(
    [string]$subID = ''
)

az ad sp create-for-rbac --name "githubActions" --role contributor `
                            --scopes /subscriptions/$subID `
                            --sdk-auth