# swapi-uservice
A tiny microservice to interact with the Star Wars API (https://swapi.dev/), fetching the data from **people** endpoint and returning it sorted by **name**

The microservice is written in Python and containerized with Docker, orchestrated with Docker Compose and deployed to a local Kubernetes cluster (Minikube)

## Requirements
Python

Docker

Docker Compose

Minikube

## How-to
Clone the repo first, then:

###   option 1 - run service with Docker Compose
- run 'docker-compose up --build'
- get the data by web browsing to **http://localhost:8000/people**
### option 2 - deploy service in local k8s cluster (Minikube)
- start Minikube
- Apply Deployment and Service:
  run 'kubectl apply -f deployment.yaml'
  run 'kubectl apply -f service.yaml'
- Expose the service
  run 'minikube service swapi-service'
- It will open the browser with yout Minikube ip address and external port 30007. Then just add **/people** endopoint to get the data
  
  
  


