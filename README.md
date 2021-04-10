Warehouse Service
==================

> A microservice written in [Python3](https://www.python.org/download/releases/3.0/) for being used for a DevOps assessment.

Warehouse service: saves products by category and with a unique id in a NoSQL database, consult the existing products as many times as you want.

### Built with

- [Python3](https://www.python.org/download/releases/3.0/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

Getting started
---------------

### Prerequisites

- [Docker](https://www.docker.com/)
- [Apache CouchDB](http://couchdb.apache.org)
  ```sh
  docker run --rm -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=pass -p 5984:5984 couchdb
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/andresr22/warehouse_service.git
   ```
2. Install dependencies
   ```sh
   pip3 install -r requirements
   pip3 install connexion[swagger-ui]
   ```

3. Run the service
   ```sh
   python3 app.py
   ```

Usage
-----
API Documentation [Swagger](https://swagger.io/)
```
http://localhost:8080/v1/ui
```

### Add product
```
POST /v1/products/createProduct
```
```json
{
  "_id": "string",
  "category": "string",
  "prodname": "string",
  "quantity": 0
}
```

### Get product

```
GET /products/getproduct/{prodId}
```

Contributing
---------------

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

## Contact

Andres Rios - [LinkedIn](https://www.linkedin.com/in/andresriosgtz/) - andres.rios@honeywell.com
