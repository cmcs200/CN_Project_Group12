#!/bin/sh
#alias kubectl="minikube kubectl --"
# get mongo taxi pod name
PNAME1=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=mongo-taxi)
PNAME2=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=mongo-taxi-ptt)
PNAME3=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=mongo-taxi-tt)
PIP=$(kubectl describe svc mongo-s | grep -Po 'Endpoints:\s\K.*' | tr -d " \t\n\r")
PIPTT=$(kubectl describe svc mongo-tt-s | grep -Po 'Endpoints:\s\K.*' | tr -d " \t\n\r")
PIPPTT=$(kubectl describe svc mongo-ptt-s | grep -Po 'Endpoints:\s\K.*' | tr -d " \t\n\r")

# copy yellow_tripdata_2016-03.csv to mongo taxi pod
kubectl cp database/import.sh ${PNAME1}:/home/import.sh
kubectl cp database/import.sh ${PNAME2}:/home/import.sh
kubectl cp database/import.sh ${PNAME3}:/home/import.sh
kubectl cp database/yellow_tripdata_2016-03.csv ${PNAME1}:/home/data.csv
kubectl cp database/data_payType_totalAmount_tripDistance.csv ${PNAME2}:/home/data.csv
kubectl cp database/data_tpep_tipAmount.csv ${PNAME3}:/home/data.csv

# import data into taxisdb
kubectl exec deployment/mongo-taxi -it -- /bin/bash -c "chmod +x ./home/import.sh && ./home/import.sh ${PIP}" 
kubectl exec deployment/mongo-taxi-ptt -it -- /bin/bash -c "chmod +x ./home/import.sh && ./home/import.sh ${PIPPTT}" 
kubectl exec deployment/mongo-taxi-tt -it -- /bin/bash -c "chmod +x ./home/import.sh && ./home/import.sh ${PIPTT}" 


