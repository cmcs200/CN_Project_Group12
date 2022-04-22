#!/bin/sh

# prometheus deployment and config
kubectl apply -f kubernetes_deployment/prom-comp.yaml
kubectl apply -f kubernetes_deployment/py-prom-d.yaml
kubectl apply -f kubernetes_deployment/py-prom-s.yaml
kubectl create configmap prometheus-cm --from-file kubernetes_deployment/prometheus-cm.yml
kubectl apply -f kubernetes_deployment/prometheus.yaml

# k8s-dashboard deployment and config
kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.5.0/aio/deploy/recommended.yaml
kubectl create serviceaccount dashboard-admin-sa 
kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa
kubectl get secret $(kubectl get serviceaccount dashboard-admin-sa -o jsonpath="{.secrets[0].name}") -o jsonpath="{.data.token}" | base64 --decode > kubernetes_deployment/secret_token.txt

# configure the services in kubernetes
kubectl apply -f kubernetes_deployment/rbac.yaml --record
kubectl apply -f kubernetes_deployment/mongo-secret.yaml --record
kubectl apply -f kubernetes_deployment/persist-vol.yaml --record
kubectl apply -f kubernetes_deployment/pv-claim.yaml --record
kubectl apply -f kubernetes_deployment/deployment_DB.yaml --record
kubectl apply -f kubernetes_deployment/deployment_provider.yaml --record
kubectl apply -f kubernetes_deployment/deployment_Analysis.yaml --record
kubectl apply -f kubernetes_deployment/ingress.yaml --record
kubectl apply -f kubernetes_deployment/grafana.yaml --record

echo "
Access Prometheus: http://localhost:8080
"
chmod +x ./kubernetes_deployment/prometheus-pf.sh &
./kubernetes_deployment/prometheus-pf.sh &

echo "
Or you can use Grafana at: http://localhost:8081
"
chmod +x ./kubernetes_deployment/grafana-pf.sh &
./kubernetes_deployment/grafana-pf.sh &

# access k8s-dashboard
echo "
Access Kubernetes-Dashboard: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login
"
kubectl proxy &

# databases ingestion in mongoDB
sleep 120
chmod +x kubernetes_deployment/mongo-data-ingestion.sh 
./kubernetes_deployment/mongo-data-ingestion.sh 

echo "
Kubernetes Configured Successfully! If there was an error in injection of the database, wait a few minutes and run ./kubernetes_deployment/mongo-data-ingestion.sh, please
"
&& fg

