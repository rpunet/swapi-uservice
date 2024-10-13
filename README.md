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

  ### option 1 - run service with Docker Compose
  - run *docker-compose up --build*
  - get the data by web browsing to **http://localhost:8000/people**
  ### option 2 - deploy service in local k8s cluster (Minikube)
  - start Minikube

    run *minikube start*
  - apply Deployment and Service:

    run *kubectl apply -f deployment.yaml*

    run *kubectl apply -f service.yaml*
  - expose the service:

    run *minikube service swapi-service*
  - it will open the browser with yout Minikube ip address and external port 30007. Then just add **/people** endopoint to the URL to get the data


## Run Performance test simulating load
- Deploy the application:
  - *minikube start*
    
  - *kubectl apply -f deployment.yaml*
     
  - *kubectl apply -f service.yaml*
     
  - *kubectl apply -f hpa.yaml*
     
- Run the performance test (you can edit the test.py to configure the number of concurrent requests and duration of the test)
  
  - *python test.py*
    
- When the CPU for containers defined in *deployment.yaml* reach utilization defined in the HPA target (60%), the HPA will **scale up** creating new pods and k8s will rebalance the load between them. You can monitor the replicas number and the utilization percentage by running:

  - *kubectl get hpa*
    
- When the CPU usage decreases, the HPA will automatically **scale down** the number of pods


  
  
  


