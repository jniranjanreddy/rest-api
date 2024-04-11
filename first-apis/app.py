from flask import Flask, request

app = Flask(__name__)

items = [
    {
    "name": "Green Apple Mojito",
    "price": 100
    },
    {
    "name": "Virgin Mojito",
    "price": 150
    }

]


@app.get('/get-items') ## http://127.0.0.1:5000/get-items

def get_items():
    return {"items": items}

## Post Request
@app.post('/add-item') ## http://127.0.0.1:5000/add-items

def add_item():
    request_data = request.get_json()
    items.append(request_data)
    return {"Message": "Item added successfully"}, 201
    
