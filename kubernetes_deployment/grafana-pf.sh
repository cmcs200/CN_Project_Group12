PNAME=$(kubectl get pods --template '{{range .items}}{{.metadata.name}}{{end}}' --selector=app=grafana)
kubectl port-forward ${PNAME} 8081:3000
