#! /bin/bash

sleep 3
num=$(mongo mongodb://$1/taxisdb --eval "db.stats().objects" --quiet)
echo $num
if [[ $num -eq 0 ]]
then mongoimport --host $1 -u 'grupo12' -p 'kubernetes' --authenticationDatabase admin --db taxisdb --collection taxis --type csv --file /home/data_ptt.csv --headerline
fi
echo "done"
