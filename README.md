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

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/omarvicentinho1/devops-challenge.git
   ```
2. Create container for app and database
   ```sh
   cd /devops-challenge
   ./start.sh
   (sudo) chmod +x start.sh (execute if you have a permission error)
   ```

3. Check the service
   ```sh
   http://localhost:8080
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
