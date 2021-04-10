import requests
import couchdb
from couchdb import http, json, util

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'pass'
COUCHDB_URL = 'http://{}:{}@localhost:5984/'.format(ADMIN_USERNAME, ADMIN_PASSWORD)
couch = couchdb.Server(COUCHDB_URL)

class ProductProvider(object):
    
    def create_product(self, payload):
        try:
            db = couch['products']
        except http.ResourceNotFound:
            db = couch.create('products')
        if payload['_id'] in db:
            return { "error": "An existing item already exists" }, 409
        else:
            db.save(payload)
            return payload, 201
    
    def read_product(self, prodId) -> str:
        db = couch['products']
        if prodId in db:
            product = db[prodId]
            return product, 200
        else:
            return { "error": "A product with the specified ID was not found" }, 400