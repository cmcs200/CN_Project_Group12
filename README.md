# CN_Project
Command to run: 
docker-compose up

on a different cmd populate db with 2 commands:
docker exec -it CONTAINER_ID /bin/bash
mongoimport --db taxisdb --collection taxis --type csv --file home/data.csv --headerline
