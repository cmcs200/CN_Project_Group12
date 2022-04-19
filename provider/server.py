import config 
import json
from flask_pymongo import PyMongo
from config import db
from flask import Response
from bson import json_util
import pandas as pd
import provider

connex_app = config.connex_app

connex_app.add_api("taxiAPI.yaml")

connex_app.route("/provider",methods=["GET"])

connex_app.route("/provider/{c_name}", methods=["GET", "DELETE"])

connex_app.route("/provider/pickUpDateTime/{start}/dropOffDateTime/{end}", methods=["GET", "DELETE"])

connex_app.route("/provider/{record}", methods=["POST"])

connex_app.route("/health",methods=["GET"])

if __name__ == '__main__':
	connex_app.run(debug=True, host='0.0.0.0',use_reloader=False)
