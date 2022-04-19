#!/bin/sh

sleep 3
num=$(mongo mongodb://mongo-s:27017/taxisdb --eval "db.stats().objects" --quiet)
echo $num
if [ $num -eq 0 ]
then mongoimport --host mongo_taxi:27017 --db taxisdb --collection taxis --type csv --file /home/data.csv --headerline
fi
echo "done"
