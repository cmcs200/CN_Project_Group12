from pymongo import MongoClient
import os
import connexion


from flask_pymongo import PyMongo



basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__,specification_dir=basedir)
app = connex_app.app


app.config["MONGO_URI"] = "mongodb://mongo_taxi:27017/taxisdb"
mongodb_client = PyMongo(app)
db = mongodb_client.db

