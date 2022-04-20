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

