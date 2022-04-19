#!/bin/sh

# get mongo taxi pod name
PNAME=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=mongo-taxi)

# copy yellow_tripdata_2016-03.csv to mongo taxi pod
kubectl cp database/yellow_tripdata_2016-03.csv ${PNAME}:/home/data.csv

# import data into taxisdb
kubectl exec deployment/mongo-taxi -it -- /bin/bash -c "mongoimport --authenticationDatabase admin --host mongo-s --port 27017 -u 'grupo12' -p 'kubernetes' --db taxisdb --collection taxis --type csv --file /home/data.csv --headerline"