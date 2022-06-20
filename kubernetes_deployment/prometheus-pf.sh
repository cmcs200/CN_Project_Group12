#alias kubectl="minikube kubectl --"
PNAME=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=prometheus)
kubectl port-forward ${PNAME} 8080:9090
