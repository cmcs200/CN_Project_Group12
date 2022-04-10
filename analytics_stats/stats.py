import pandas as pd
from flask import request
import connexion
import json
from datetime import datetime #jr: add
from sklearn.preprocessing import LabelEncoder #jr: add
from scipy.stats import f_oneway #jr: add
import statistics
import numpy as np
from messages_pb2 import ClientRequest
from messages_pb2_grpc import ClientProviderRequestStub
import grpc

messages_channel = grpc.insecure_channel("server:50051")
messages_client = ClientProviderRequestStub(messages_channel)


def continouousAnalytics(p_id,c_name):
    if((p_id==1 or p_id==2) and c_name in ["passenger_count","trip_distance","fare_amount", "extra", "tip_amount", "tolls_amount","total_amount"]):

        data_from_DB=callDB(c_name)
		
        dictionary={}
        filteredDataFrame=data_from_DB.loc[data_from_DB["VendorID"] == p_id]

        dictionary["mean"] = statistics.mean(filteredDataFrame[c_name])
        dictionary["max"] = max(filteredDataFrame[c_name])
        dictionary["min"] = min(filteredDataFrame[c_name])
        dictionary["standard_deviation"] = np.std(filteredDataFrame[c_name])
        dictionary["mode"] = statistics.mode(filteredDataFrame[c_name])
        return json.dumps(dictionary),200
    pass


def categoricalAnalytics(p_id,c_name):
    if((p_id==1 or p_id==2) and c_name in ["payment_type","RatecodeID"]):
        data_from_DB=callDB(c_name) 
        filteredDataFrame=data_from_DB.loc[data_from_DB["VendorID"] == p_id]
        seriesValues=None
        if c_name=="payment_type":
            pt_dict ={1:"Credit Card",2: "Cash", 3:"No charge", 4:"Dispute",5:"Unknown",6:"Voided trip"}
            seriesValues=filteredDataFrame[c_name].value_counts(normalize=True).rename(index=pt_dict)
        if c_name=="RatecodeID":
            rc_dict={1:"Standard rate",2:"JFK",3:"Newark",4:"Nassau or Westchester",5:"Negotiated fare",6:"Group ride"}           
            seriesValues=filteredDataFrame[c_name].value_counts(normalize=True).rename(index=rc_dict)
        return json.dumps(seriesValues.to_dict())     
    if((p_id==1 or p_id==2) and c_name in ["tpep_pickup_datetime","tpep_dropoff_datetime"]):
        data_from_DB=callDB(c_name) 
        filteredDataFrame=data_from_DB.loc[data_from_DB["VendorID"] == p_id]
        datetime = pd.to_datetime(filteredDataFrame[c_name]) # series to datetime
        time = datetime.dt.strftime('%H:%M') # extract only time
        time_int = time.apply(lambda date: int(date[:2])) # time to integer extracting only hour
        filteredDataFrame[c_name] = time_int

        dictionary={}
        dictionary["mean"] = round(statistics.mean(filteredDataFrame[c_name]))
        dictionary["max"] = max(filteredDataFrame[c_name])
        dictionary["min"] = min(filteredDataFrame[c_name])
        dictionary["standard_deviation"] = np.std(filteredDataFrame[c_name])
        dictionary["mode"] = statistics.mode(filteredDataFrame[c_name])


        filteredDataFrame[c_name] = filteredDataFrame[c_name].apply(lambda date: "00h-03h" if 0 <= date <= 3 
                                                                                    else "04h-07h" if 4 <= date <= 7 
                                                                                    else "08h-11h" if 8 <= date <= 11
                                                                                    else "12h-15h" if 12 <= date <= 15
                                                                                    else "16h-19h" if 16 <= date <= 19
                                                                                    else "20h-23h") # discretize
        dictionary.update(filteredDataFrame[c_name].value_counts(normalize=True))

        return json.dumps(dictionary),200
    pass

def callDB(column):
    listDB=json.loads(messages_client.DBMakeRequest(ClientRequest(request=["VendorID",column])).response)
    return pd.DataFrame(listDB)