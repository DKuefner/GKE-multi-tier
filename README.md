Based on : https://github.com/velotio-tech/GKE-and-Sample-App

Simple two tier demo app with webapp as frontend and MySQL as backend.
This app is intended as a demo and to be deployed on a specific GKE environment, however, it can be easily adopted to run on other Kubernetes environments.
You can use curl to write and read entries to database.
Sample commands:
Write data
curl -H "Content-Type: application/x-www-form-urlencoded" -X POST http://<ext-ip-addr>:80/storedata -d id=<int>1 -d name=<string>
Read data
curl <ext-ip-addr>:80/getdata/1


GKE Autopilot Cluster
How to deploy app to Autopilot Cluster
 
Deployments
* Volumes
    +mysql-pv.yaml
*MySQL-DB
    +mysql-deployment.yaml
*Web app
    +webapp-deployment.yaml
Services
*MySQL Service
    +mysql-service.yaml
*Web app Service
    +webapp-service.yaml
Persistent Disk (GCE  Storage  Disks)
*pdName: team2-pd
