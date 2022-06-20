# import libraries
from pyexpat.errors import messages
from numpy import around
import pandas as pd
from flask import render_template
import grpc
import json
from datetime import datetime 
from sklearn.preprocessing import LabelEncoder
from scipy.stats import f_oneway
from messages_pb2 import ClientRequest
from messages_pb2_grpc import ClientProviderRequestStub
import pybreaker

messages_channel = grpc.insecure_channel("provider-s:50051")
messages_client = ClientProviderRequestStub(messages_channel)
db_breaker=pybreaker.CircuitBreaker(fail_max=2, reset_timeout=60)

def health():
	return 200

# function to get a proper answer depending on the p-value
def getPValueAnswer(p_value,var1,var2):

    response_dictionary = {}
    response_dictionary["ANOVA Test P-value"] = p_value

    if p_value <= 0.05:
        response = "As the output of the P-value is less than 0.05, hence, we reject H0. Which means the variables "\
         + var1 + " and " + var2 + " are correlated with each other."
            
        response_dictionary["Response"] = response

        return json.dumps(response_dictionary)

    else:
        response = "As the output of the P-value is greater than 0.05, hence, we don't reject H0. Which means the variables "\
         + var1 + " and " + var2 + " are not correlated with each other."
            
        response_dictionary["Response"] = response

        return json.dumps(response_dictionary)



def correlation_dateTime_distance():
    data_from_DB=callDB("tpep_pickup_datetime","trip_distance")

    datetime = pd.to_datetime(data_from_DB["tpep_pickup_datetime"]) # series to datetime
    time = datetime.dt.strftime('%H:%M') # extract only time
    time_int = time.apply(lambda date: int(date[:2])) # time to integer extracting only hour

    # discretize
    time_disc = time_int.apply(lambda date: "00h-03h" if 0 <= date <= 3 
                                                else "04h-07h" if 4 <= date <= 7 
                                                else "08h-11h" if 8 <= date <= 11
                                                else "12h-15h" if 12 <= date <= 15
                                                else "16h-19h" if 16 <= date <= 19
                                                else "20h-23h") 

    data_from_DB["tpep_pickup_datetime"] = time_disc


    # f_oneway() function takes the group data as input and 
    # returns F-statistic and P-value

    # Running the one-way anova test between trip_distance and pickup_datetime
    # Assumption(H0) is that pickup_datetime and trip_distance are NOT correlated

    # Finds out the trip_distance data for each pickup_datetime as a list
    enc = LabelEncoder()
    data_from_DB["tpep_pickup_datetime"] = enc.fit_transform( data_from_DB["tpep_pickup_datetime"])

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    p_value = f_oneway(data_from_DB["tpep_pickup_datetime"], data_from_DB["trip_distance"])[1]

    return getPValueAnswer(p_value,"tpep_pickup_datetime", "trip_distance")



def correlation_payment_type_tip():
    data_from_DB=callDB("payment_type","tip_amount")

    # Finds out the tip_amount data for each payment_type as a list
    CategoryGroupLists= data_from_DB.groupby("payment_type")["tip_amount"].apply(list)

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    p_value = f_oneway(*CategoryGroupLists)[1]
    
    return getPValueAnswer(p_value,"payment_type", "tip")



def correlation_payment_type_total_amount():
    data_from_DB=callDB("payment_type","total_amount")

    # Finds out the tip_amount data for each payment_type as a list
    CategoryGroupLists= data_from_DB.groupby("payment_type")["total_amount"].apply(list)

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    stat, p_value = f_oneway(*CategoryGroupLists)
    
    return getPValueAnswer(p_value,"payment_type", "total_amount")



def correlation_dateTime_payment_type():
    data_from_DB=callDB("tpep_pickup_datetime", "payment_type")

    datetime = pd.to_datetime(data_from_DB["tpep_pickup_datetime"]) # series to datetime
    time = datetime.dt.strftime('%H:%M') # extract only time
    time_int = time.apply(lambda date: int(date[:2])) # time to integer extracting only hour

    # discretize
    time_disc = time_int.apply(lambda date: "00h-03h" if 0 <= date <= 3 
                                                else "04h-07h" if 4 <= date <= 7 
                                                else "08h-11h" if 8 <= date <= 11
                                                else "12h-15h" if 12 <= date <= 15
                                                else "16h-19h" if 16 <= date <= 19
                                                else "20h-23h") 

    data_from_DB["tpep_pickup_datetime"] = time_disc

    # f_oneway() function takes the group data as input and 
    # returns F-statistic and P-value

    # Running the one-way anova test between trip_distance and pickup_datetime
    # Assumption(H0) is that pickup_datetime and trip_distance are NOT correlated

    # categorical variables encoding
    enc = LabelEncoder()
    data_from_DB["tpep_pickup_datetime"] = enc.fit_transform( data_from_DB["tpep_pickup_datetime"])
    data_from_DB["payment_type"] = enc.fit_transform( data_from_DB["payment_type"])

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    p_value = f_oneway(data_from_DB["tpep_pickup_datetime"], data_from_DB["payment_type"])[1]

    return getPValueAnswer(p_value,"tpep_pickup_datetime", "payment_type")



def correlation_totalAmmount_tip():
    data_from_DB=callDB("total_amount", "tip_amount")

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    p_value = f_oneway(data_from_DB["total_amount"], data_from_DB["tip_amount"])[1]
    
    return getPValueAnswer(p_value,"total_amount", "tip_amount")



def correlation_tripDistance_tip():
    data_from_DB=callDB("trip_distance", "tip_amount")

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    p_value = f_oneway(data_from_DB["trip_distance"], data_from_DB["tip_amount"])[1]
    
    return getPValueAnswer(p_value,"trip_distance", "tip_amount")


@db_breaker
def callDB(column1,column2):
    listDB=json.loads(messages_client.DBMakeRequest(ClientRequest(request=[column1,column2])).response)
    return pd.DataFrame(listDB)
