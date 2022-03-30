import config 
import json
from flask_pymongo import PyMongo
from config import db
from flask import Response
from bson import json_util
import pandas as pd

connex_app = config.connex_app

connex_app.add_api("taxiAPI.yaml")

connex_app.route("/provider/{p_id}/analytics/{c_name}",methods=["GET"])

connex_app.route("/provider/{p_id}/stats/{c_name}", methods=["GET"])#delete funciona sem por????

if __name__ == '__main__':
	connex_app.run(debug=True, host='0.0.0.0',port=5001,use_reloader=False)
