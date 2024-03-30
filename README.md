# datadots

## Getting started

Run app locally with docker 
```bash
docker build -t vkehayov .
docker run -p 5000:5000 vkehayov
```

Download docker image from docker hub and test locally
```bash
docker pull dirrrr/dd:latest
docker run -p 5000:5000 dirrrr/dd:latest
```

For both cases go to your browser on address 127.0.0.1:5000 and the app should open.

It is a simple flask app which once you provide `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY`. 
It will calculate the bill for the specified period. 
The second which will show you are Client and Public IP addresses.


Run the application as a Kubernetes deployment
```bash
kubectl apply -f k8s/deployment.yaml
kubectl port-forward deployment/datadots-vkehayov 5000:5000

## Once you are done testing

kubectl delete -f k8s/deployment.yaml
```