import os
import connexion

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__,specification_dir=basedir)

connex_app.add_api("taxiAPI.yaml")

connex_app.route("/correlation_dateTime_distance",methods=["GET"])

connex_app.route("/correlation_payment_type_tip", methods=["GET"])

connex_app.route("/correlation_payment_type_total_amount", methods=["GET"])

connex_app.route("/correlation_dateTime_payment_type", methods=["GET"])

connex_app.route("/correlation_totalAmmount_tip", methods=["GET"])

connex_app.route("/correlation_tripDistance_tip", methods=["GET"])


if __name__ == '__main__':
	connex_app.run(debug=True, host='0.0.0.0',port=5002,use_reloader=False)
