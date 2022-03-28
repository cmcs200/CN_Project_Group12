import pandas as pd
from flask import render_template
import connexion
import json
from datetime import datetime #jr: add
from sklearn.preprocessing import LabelEncoder #jr: add
from scipy.stats import f_oneway #jr: add

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file to configure the endpoints
app.add_api("taxiApi.yml")


# create a URL route in our application for "/"
@app.route("/correlations/dateTime_distance")
def correlation_dateTime_distance():
    data_from_DB=callDB()
    data_from_DB["tpep_pickup_datetime"] = datetime.strptime(data_from_DB["tpep_pickup_datetime"], '%Y-%m-%d-%H-%M').time() #time
    
    data_from_DB["tpep_pickup_datetime"] = data_from_DB["tpep_pickup_datetime"].date.apply(lambda date: int(date[:2])) #numerical

    data_from_DB["tpep_pickup_datetime"] = data_from_DB["tpep_pickup_datetime"].date_numeric.apply(lambda date: "00h-03h" if 0 <= date <= 3 
                                                                                    else "04h-07h" if 4 <= date <= 7 
                                                                                    else "08h-11h" if 8 <= date <= 11
                                                                                    else "12h-15h" if 12 <= date <= 15
                                                                                    else "16h-19h" if 16 <= date <= 19
                                                                                    else "20h-23h") # discretize

    # f_oneway() function takes the group data as input and 
    # returns F-statistic and P-value

    # Running the one-way anova test between trip_distance and pickup_datetime
    # Assumption(H0) is that pickup_datetime and trip_distance are NOT correlated

    # Finds out the trip_distance data for each pickup_datetime as a list
    CategoryGroupLists= data_from_DB.groupby("tpep_pickup_datetime")["trip_distance"].apply(list)

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    _, p_value = f_oneway(*CategoryGroupLists)
    
    return getPValueAnswer(p_value,"tpep_pickup_datetime", "trip_distance")
	
@app.route("/correlations/paymentType_tip")
def correlation_paymentType_tip():
    data_from_DB=callDB()
    CategoryGroupLists= data_from_DB.groupby("paymentType")["tip"].apply(list)

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    _, p_value = f_oneway(*CategoryGroupLists)
    
    return getPValueAnswer(p_value,"paymentType", "tip")

@app.route("/correlations/paymentType_totalAmmount")
def correlation_paymentType_totalAmmount():
    data_from_DB=callDB()
    CategoryGroupLists= data_from_DB.groupby("paymentType")["totalAmmount"].apply(list)

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    _, p_value = f_oneway(*CategoryGroupLists)
    
    return getPValueAnswer(p_value,"paymentType", "totalAmmount")

@app.route("/correlations/dateTime_paymentType")
def correlation_dateTime_distance():
    data_from_DB=callDB()
    data_from_DB["tpep_pickup_datetime"] = datetime.strptime(data_from_DB["tpep_pickup_datetime"], '%Y-%m-%d-%H-%M').time() #time
    
    data_from_DB["tpep_pickup_datetime"] = data_from_DB["tpep_pickup_datetime"].date.apply(lambda date: int(date[:2])) #numerical

    data_from_DB["tpep_pickup_datetime"] = data_from_DB["tpep_pickup_datetime"].date_numeric.apply(lambda date: "00h-03h" if 0 <= date <= 3 
                                                                                    else "04h-07h" if 4 <= date <= 7 
                                                                                    else "08h-11h" if 8 <= date <= 11
                                                                                    else "12h-15h" if 12 <= date <= 15
                                                                                    else "16h-19h" if 16 <= date <= 19
                                                                                    else "20h-23h") # discretize

    # f_oneway() function takes the group data as input and 
    # returns F-statistic and P-value

    # Running the one-way anova test between trip_distance and pickup_datetime
    # Assumption(H0) is that pickup_datetime and trip_distance are NOT correlated

    # Finds out the trip_distance data for each pickup_datetime as a list
    CategoryGroupLists= data_from_DB.groupby("tpep_pickup_datetime")["paymentType"].apply(list)

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    _, p_value = f_oneway(*CategoryGroupLists)
    
    return getPValueAnswer(p_value,"tpep_pickup_datetime", "paymentType")

@app.route("/correlations/totalAmmount_tip")
def correlation_totalAmmount_tip():
    data_from_DB=callDB()
    filteredDataFrame=data_from_DB["totalAmount","tip"]
    dictionary={"Correlation value": filteredDataFrame.corr()}
    CategoryGroupLists= data_from_DB.groupby("paymentType")["totalAmmount"].apply(list)

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    _, p_value = f_oneway(*CategoryGroupLists)
    
    return getPValueAnswer(p_value,"paymentType", "totalAmmount",dictionary)

@app.route("/correlations/tripDistance_tip")
def correlation_tripDistance_tip():
    data_from_DB=callDB()
    filteredDataFrame=data_from_DB["tripDistance","tip"]
    dictionary={"Correlation value": filteredDataFrame.corr()}
    CategoryGroupLists= data_from_DB.groupby("paymentType")["totalAmmount"].apply(list)

    # Performing the ANOVA test
    # We accept the Assumption(H0) only when P-Value &gt; 0.05
    _, p_value = f_oneway(*CategoryGroupLists)
    
    return getPValueAnswer(p_value,"paymentType", "totalAmmount",dictionary)
    
def getPValueAnswer(p_value,var1,var2,dict):
    if (dict!=None):
        response_dictionary=dict
    else:
        response_dictionary={}
    response_dictionary["P-value"] = p_value
    if p_value <= 0.05:
        response = "As the output of the P-value is less than 0.05, hence, \
            we reject H0. Which means the variables " + var1 + " and " + var2 + " are correlated with each other."
            
        response_dictionary["Response"] = response

        return json.dumps(response_dictionary)

    else:
        response = "As the output of the P-value is greater than 0.05, hence, \
            we don't reject H0. Which means the variables " + var1 + " and " + var2 + " are not correlated with each other."
            
        response_dictionary["Response"] = response

        return json.dumps(response_dictionary) 

def callDB():

    return result

if __name__ == "__analytics__":
    app.run(debug=True)
