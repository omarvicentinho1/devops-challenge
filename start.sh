#!/bin/bash
sudo docker run -d --name warehouse_service -p 8080:8080 omarvicentinho1/devops-challenge
sudo docker run --rm -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=pass -p 5984:5984 couchdb

