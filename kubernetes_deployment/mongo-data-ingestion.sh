#!/bin/sh

# get mongo taxi pod name
PNAME=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=mongo-taxi)
PIP=$(kubectl describe svc mongo-s | grep -Po 'Endpoints:\s\K.*' | tr -d " \t\n\r")

# copy yellow_tripdata_2016-03.csv to mongo taxi pod
kubectl cp database/import.sh ${PNAME}:/home/import.sh
kubectl cp database/yellow_tripdata_2016-03.csv ${PNAME}:/home/data.csv

# import data into taxisdb
kubectl exec deployment/mongo-taxi -it -- /bin/bash -c "./home/import.sh ${PIP}" 
