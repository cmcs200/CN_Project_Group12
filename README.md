<img src="https://ciencias.ulisboa.pt/sites/default/files/Ciencias_Logo_Azul-01.png" width="250" height="130">

# Cloud Computing Final Project
<!--  -->
 * Cristiano Santos
 * João Raimundo
 * João Rato
<!--  -->

<br>

In this checkpoint of the implementation, each microservice is deployed in a docker container. gRPC were implemented to insure the communication between microservices.
Addicionally, all the containers are orchestrated in Kubernetes. 

<!-- How to deploy: -->

To set and configure Kubernetes with the microservices containers orchestrated run the command:

```
$ ./deploy_kubernetes.sh
```




Command to run: 
docker-compose up

on a different cmd populate db with 2 commands:
docker exec -it CONTAINER_ID /bin/bash
mongoimport --db taxisdb --collection taxis --type csv --file home/data.csv --headerline

csv in database folder is incomplete for test purposes.
to get the full csv file get it on https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data?resource=download&select=yellow_tripdata_2016-03.csv
