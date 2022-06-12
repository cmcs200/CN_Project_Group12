from pymongo import MongoClient
import os
import connexion


from flask_pymongo import PyMongo



basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__,specification_dir=basedir)
app = connex_app.app


app.config["MONGO_URI"] = "mongodb://grupo12:kubernetes@deployment/mongo-taxi:27017/taxisdb?authSource=admin"
uri = "mongodb://grupo12:kubernetes@mongo-s:27017/taxisdb?authSource=admin"
client = MongoClient(uri)
db = MongoClient(uri).get_database()

app.config["MONGO_URI_ptt"] = "mongodb://grupo12:kubernetes@deployment/mongo-taxi-ptt:27018/taxisdb?authSource=admin"
uri_ptt = "mongodb://grupo12:kubernetes@mongo-ptt-s:27018/taxisdb?authSource=admin"
client_ptt = MongoClient(uri_ptt)
db_ptt = MongoClient(uri_ptt).get_database()

app.config["MONGO_URI_tt"] = "mongodb://grupo12:kubernetes@deployment/mongo-taxi-tt:27019/taxisdb?authSource=admin"
uri_tt = "mongodb://grupo12:kubernetes@mongo-tt-s:27019/taxisdb?authSource=admin"
client_tt = MongoClient(uri_tt)
db_tt = MongoClient(uri_tt).get_database()

