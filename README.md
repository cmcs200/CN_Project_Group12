<img src="https://ciencias.ulisboa.pt/sites/default/files/Ciencias_Logo_Azul-01.png" width="250" height="130">

# Cloud Computing Final Project

 * Cristiano Santos
 * João Raimundo
 * João Rato


<br>

In this checkpoint of the implementation, each microservice is deployed in a docker container. gRPC were implemented to insure the communication between microservices.
Addicionally, all the containers are orchestrated in Kubernetes. 

<br>

### How to deploy: 

To set and configure Kubernetes with the microservices containers orchestrated run the command:

```
$ ./deploy_kubernetes.sh
```

<br>

### Kubernetes-Dashboard: 

<br>

Kubernetes-Dashboard is accessible on : 

 * http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

Use the secret token that is on `kubernetes_deployment/secret_token.txt` to login into the dashboard.

<br>

### Prometheus: 

<br>

Prometheus is accessible on : 
 * http://localhost:31218/targets

<br>

