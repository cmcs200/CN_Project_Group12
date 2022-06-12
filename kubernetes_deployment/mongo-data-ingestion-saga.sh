#!/bin/sh

# get mongo taxi pod name
PNAME1=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=mongo-taxi)
PNAME2=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=mongo-taxi-ptt)
PNAME3=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=mongo-taxi-tt)
PIP=$(kubectl describe svc mongo-s | grep -Po 'Endpoints:\s\K.*' | tr -d " \t\n\r")

# copy yellow_tripdata_2016-03.csv to mongo taxi pod
kubectl cp database/import.sh ${PNAME1}:/home/import.sh
kubectl cp database/import_data_ptt.sh ${PNAME2}:/home/import.sh
kubectl cp database/import_data_tt.sh ${PNAME3}:/home/import.sh
kubectl cp database/yellow_tripdata_2016-03.csv ${PNAME1}:/home/data.csv
kubectl cp database/data_payType_totalAmount_tripDistance.csv ${PNAME2}:/home/data_ptt.csv
kubectl cp database/data_tpep_tipAmount.csv ${PNAME3}:/home/data_tt.csv

# import data into taxisdb
kubectl exec deployment/mongo-taxi -it -- /bin/bash -c "./home/import.sh ${PIP}" 
kubectl exec deployment/mongo-taxi-ptt -it -- /bin/bash -c "./home/import.sh ${PIP}" 
kubectl exec deployment/mongo-taxi-tt -it -- /bin/bash -c "./home/import.sh ${PIP}" 


