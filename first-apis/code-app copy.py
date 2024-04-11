from flask import Flask, request

app = Flask(__name__)

items = {
        "f87498038e0044f3bb49add503aa1520":{
                                            "name": "apple",
                                            "price": 100
                                           },
        "f87498038e0044f3bb49add503aa1521":{
                                            "name": "orange",
                                            "price": 200
                                           } 
}

## GET Items
@app.get('/items') ## http://127.0.0.1:5000/get-items
def get_items():
    return {"items": items}

# ## One way to get item # http://127.0.0.1:5000/get-items/apple
# @app.get('/get-item/<string:name>') ## http://127.0.0.1:5000/get-items
# def get_item(name):
#     for item in items:
#         if name == item['name']:
#             return item
#     return {"Message": "Item not found"}, 400

## GET another way to get item through postman # http://127.0.0.1:5000/get-item?name=orange
@app.get('/item') ## http://127.0.0.1:5000/get-items
def get_item():
    name = request.args.get('name')
    print(name)
    for item in items:
        if name == item['name']:
            return item
    return {"Message": "Item not found"}, 400

## POST Request
@app.post('/item') ## http://127.0.0.1:5000/add-items
def add_item():
    request_data = request.get_json()
    items.append(request_data)
    return {"Message": "Item added successfully"}, 201
    

## Update Request

@app.put('/item') ## http://127.0.0.1:5000/add-items
def update_item():
    request_data = request.get_json()
    for item in items:
        if item['name'] == request_data['name']:
            item['price'] = request_data['price']
            return {"Message": "Item updated successfully"}, 200
    return {"Message": "Record Doesnt Exist"}, 201


@app.delete('/item') ## http://127.0.0.1:5000/get-items
def delete_item():
    name = request.args.get('name')
    for item in items:
        if name == item['name']:
            items.remove(item)
            return { "Message": "Item deleted successfully"}, 200
    return {"Message": "Item not found"}, 404