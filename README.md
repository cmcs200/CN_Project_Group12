![alt text](https://ciencias.ulisboa.pt/sites/default/files/Ciencias_Logo_Azul-01.png =250x250)

# CN_Project
Command to run: 
docker-compose up

on a different cmd populate db with 2 commands:
docker exec -it CONTAINER_ID /bin/bash
mongoimport --db taxisdb --collection taxis --type csv --file home/data.csv --headerline

csv in database folder is incomplete for test purposes.
to get the full csv file get it on https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data?resource=download&select=yellow_tripdata_2016-03.csv
