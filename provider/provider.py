from dataclasses import replace
import string
from config import db, db_ptt, db_tt
import pymongo
import os
import connexion
import config 
import json
import messages_pb2
import messages_pb2_grpc 
from bson import json_util
from flask_pymongo import PyMongo
from flask import request
from datetime import datetime
import numpy as np
import grpc

def health():
	return 200

#request:http://localhost:5000/provider/
def get_all():
	output = []
	taxis = db.taxis.find({})
	for i in taxis:
		output.append(i)

	return json.loads(json_util.dumps(output))

#request:http://localhost:5000/provider/VendorID?cond=1
#request:curl -X GET http://localhost:5000/provider/fare_amount?cond=13 -H "Accept: application/json"
def get_column(c_name,cond):
	output = []
	if c_name in ["RatecodeID","VendorID","dropoff_latitude","dropoff_longitude","extra","fare_amount","improvement_surcharge",
    "mta_tax","passenger_count","payment_type","pickup_latitude", "pickup_longitude", "tip_amount", "tolls_amount","total_amount","tpep_dropoff_datetime",
    "tpep_pickup_datetime", "trip_distance"]:
		taxis = db.taxis.find({c_name: float(cond)}).limit(50)
		for i in taxis:
			output.append(i)
		return json.loads(json_util.dumps(output)), 200
	return json.loads(json_util.dumps("Invalid colunm name.")), 404

#request:curl -X DELETE http://localhost:5000/provider/fare_amount?cond=13 -H "Accept: application/json"
def del_column(c_name, cond):
	if c_name in ["RatecodeID","VendorID","dropoff_latitude","dropoff_longitude","extra","fare_amount","improvement_surcharge",
    "mta_tax","passenger_count","payment_type","pickup_latitude", "pickup_longitude", "tip_amount", "tolls_amount","total_amount","tpep_dropoff_datetime",
    "tpep_pickup_datetime", "trip_distance"]:
		taxis = db.taxis.delete_many({c_name: float(cond)})
			
		return json.loads(json_util.dumps("Records deleted where colunm name="+c_name+"and cond="+str(cond))),200
	return json.loads(json_util.dumps("Invalid colunm name.")), 404

#http://localhost:5000/provider/pickUpDateTime/{start}/dropOffDateTime/{end}
#not working--doesnt get any results
def get_DateTime(start,end):
	output = []
	start_t=datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
	end_t=datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
	taxis = db.taxis.find({ "$and":[{"tpep_pickup_datetime" : {"$gte": start_t}}, {"tpep_dropoff_datetime": {"$lte": end_t}}]}).limit(50)
	for i in taxis:
			output.append(i)
	return json.loads(json_util.dumps(output)), 200
	
#curl -X DELETE http://localhost:5000/provider/pickUpDateTime/2016-03-01%2000:00:00/dropOffDateTime/2016-03-01%2000:00:00 -H "Accept: application/json"
def del_DateTime(start,end):
	start_t=datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
	end_t=datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
	taxis = db.taxis.delete_many({ "$and":[{"tpep_pickup_datetime" : {"$gte": start_t}}, {"tpep_dropoff_datetime": {"$lte": end_t}}]})
	if taxis.__sizeof__==0:
		return json.loads(json_util.dumps("No Record Found.")), 404		
	return json.loads(json_util.dumps("Records deleted where pickuptime was between "+start+" and "+end)),200

        
#curl -X POST http://localhost:5000/provider/provider_id=1&p_up_datetime=2016-03-01T00:00:00&d_off_datetime=2016-03-01T00:05:00&passanger_count=5&trip_distance=5.0&tariff_id=6&payment_type=2&fare_ammount=6.5
def add_record(record):
	print(record)
	#record={}
	""" start_t=datetime.strptime(p_up_datetime, '%Y-%m-%d %H:%M:%S')
	end_t=datetime.strptime(d_off_datetime, '%Y-%m-%d %H:%M:%S')
	print(isinstance(provider_id,int))
	print(isinstance(start_t,datetime))
	print(isinstance(end_t,datetime))
	print(isinstance(passanger_count,int))
	print(isinstance(trip_distance,float))
	print(isinstance(tariff_id,int))
	print(isinstance(payment_type,int))
	print(isinstance(fare_ammount,float))
	if isinstance(provider_id,int) & isinstance(start_t,datetime) & isinstance(end_t,datetime) & isinstance(passanger_count,int) & isinstance(trip_distance,float) & isinstance(tariff_id,int) & isinstance(payment_type,int) & isinstance(fare_ammount,float):
		record["provider_id"]=provider_id
		record["passanger_count"]=passanger_count
		record["trip_distance"]=trip_distance
		record["tariff_id"]=tariff_id
		record["payment_type"]=payment_type
		record["fare_ammount"]=fare_ammount """
		#db.taxis.insert_one(record)
		#return json.loads(json_util.dumps("Record was added.")), 201
	return json.loads(json_util.dumps("Request was unsuccessful"))

class ColumnsServicer(messages_pb2_grpc.ClientProviderRequestServicer):
	def DBMakeRequest(self, request, context):
		columns=request.request
		colsDict={}
		for col in columns:
			colsDict[col]=1
		#return messages_pb2.ClientResponse(response=json_util.dumps(list(db.taxis.find({},colsDict).limit(5000))))
		return messages_pb2.ClientResponse(response=json_util.dumps(list(saga(db.taxis.find({},colsDict).limit(5000), np.concatenate(db_ptt.taxis.find({},colsDict).limit(5000), db_tt.taxis.find({},colsDict).limit(5000), axis=1)))))
		

def saga(operation, compensation):
	try:
		return operation
	except grpc.StatusCode.UNKNOWN: 
		return compensation