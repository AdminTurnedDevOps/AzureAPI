# To run the Flask API inside of a container, the Docker image must exist inside of Azure Container Registry

## To build the Docker image
`docker build -t name_of_docker_image_tag .`

## To create the Azuure Container Registry

`az acr create --name name_of_acr --resource-group name_of_rg --sku Standard`

## To log into the ACR from the terminal

`az acr login --name name_of_acr`

## To tag and push the Docker image and prepare it for a push to ACR

`docker tag name_of_docker_image_tag name_of_acr.azurecr.io/azureapi/flask`
`docker push name_of_acr.azurecr.io/azureapi/flask`