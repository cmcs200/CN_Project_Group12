import os
import connexion
from flask import Response

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__,specification_dir=basedir)

connex_app.add_api("taxiAPI.yaml")

connex_app.route("/provider/{p_id}/analytics/{c_name}",methods=["GET"])

connex_app.route("/provider/{p_id}/stats/{c_name}", methods=["GET"])#delete funciona sem por????

if __name__ == '__main__':
	connex_app.run(debug=True, host='0.0.0.0',port=5001,use_reloader=False)
