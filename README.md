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

### How to access the services: 

In order to access the services through a curl, an address is needed. You can get it by executing the following command:

```
kubectl describe ingress | grep -Po 'Address:\s\K.*' | tr -d " \t\r"
```
Then, you can start using the services, like on this example, replacing the address on this link:

 * http://{address}/correlations/dateTime_distance
 
<br>

### Kubernetes-Dashboard: 

Kubernetes-Dashboard is accessible on : 

 * http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

Use the secret token that is on `kubernetes_deployment/secret_token.txt` to login into the dashboard.

<br>

### Prometheus: 

Prometheus is accessible on : 
 * http://localhost:8080/targets
