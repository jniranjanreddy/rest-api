from flask import Flask, request
import uuid
from db import items
app = Flask(__name__)

## GET Items
@app.get('/items') ## http://127.0.0.1:5000/get-items
def get_items():
    return {"items": items}

## GET another way to get item through postman
@app.get('/item') ## http://127.0.0.1:5000/get-items
def get_item():
    id = request.args.get('id')
    try:
        return items[id]
    except KeyError:
        return {"Message": "Item not found"}, 404

## POST Request
@app.post('/item') ## http://127.0.0.1:5000/add-items
def add_item():
    items[uuid.uuid4().hex] = request.get_json()
    return {"Message": "Item added successfully"}, 201
    
## Update Request
@app.put('/item') ## http://127.0.0.1:5000/add-items
def update_item():
    id = request.args.get('id')
    if id in items.keys():
        items[id] = request.get_json()
        return {"Message": "Item updated successfully"}, 200
    else:
        return {"Message": "Item not found"}, 404

## Delete Request
@app.delete('/item') ## http://127.0.0.1:5000/get-items
def delete_item():
    id = request.args.get('id')
    if id in items.keys():
        del items[id]
        return { "Message": "Item deleted successfully"}
    else:
        return {"Message": "Item not found"}, 404