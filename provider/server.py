import config 
import provider
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from concurrent import futures
import messages_pb2_grpc
import threading

connex_app = config.connex_app

connex_app.add_api("taxiAPI.yaml")

connex_app.route("/provider",methods=["GET"])

connex_app.route("/provider/{c_name}", methods=["GET", "DELETE"])

connex_app.route("/provider/pickUpDateTime/{start}/dropOffDateTime/{end}", methods=["GET", "DELETE"])

connex_app.route("/provider/{record}", methods=["POST"])


def serve():
	interceptors = [ExceptionToStatusInterceptor()]
	server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
	messages_pb2_grpc.add_ClientProviderRequestServicer_to_server(
        provider.ColumnsServicer(), server
    )
	server.add_insecure_port("0.0.0.0:50051")
	server.start()
	server.wait_for_termination()

def run_clientAPI():
	connex_app.run(debug=True, host='0.0.0.0',use_reloader=False)

if __name__ == '__main__':
	try:
		serverT=threading.Thread(target=serve)
		clientAPIT=threading.Thread(target=run_clientAPI)
		serverT.start()
		clientAPIT.start()
		serverT.join()
		clientAPIT.join()
	except:
		print("Error: unable to start thread")
	
	

	
