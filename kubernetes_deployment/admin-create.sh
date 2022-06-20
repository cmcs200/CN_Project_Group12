#!/bin/sh

#alias kubectl="minikube kubectl --"

openssl genrsa -out group12-man.key 2048

openssl req -new -key group12-man.key -out group12-man.csr

openssl x509 -req -in group12-man.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out group12-man.crt -days 500

kubectl config set-credentials group12-man --client-certificate=/root/group12-man.crt --client-key=group12-man.key

kubectl config set-context group12-man-context --cluster=kubernetes --user=group12-man
