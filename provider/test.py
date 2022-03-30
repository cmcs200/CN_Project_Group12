import requests
 
# Making a POST request
r = requests.post('http://localhost:5000/provider/{record}  post', data ={"provider_id":1,"p_up_datetime": "2016-03-01 00:00:00", "d_off_datetime":"2016-03-01 00:05:00", "passanger_count":5, "trip_distance":5.0, "tariff_id":6, "payment_type":2, "fare_ammount":6.5})
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.json())