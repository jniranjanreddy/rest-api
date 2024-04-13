from flask import Flask, request
import uuid
from db import ItemDatabase
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import ItemSchema, ItemGetSchema


blp = Blueprint("items", __name__, description="Operations on Items")


@blp.route('/item')
class Item(MethodView):
    
    def __init__(self):
        self.db = ItemDatabase()
        
    @blp.response(200, ItemGetSchema(many=True))
    # @blp.arguments(ItemOptionalQuerySchema, location="query")
    def get(self, args):
        id = args.get('id')
        if id is None:
            return self.db.get_items()
        else:
            result = self.db.get_item(id)
            if result is None:
                abort(404, message="Record doesnt exist")
            return self.db.get_item(id)
        
                
    # @blp.arguments(ItemSchema)
    # def put(self, request_data):
    #     id = args.get('id')
    #     if id == None:
    #         return {"Message": "Given ID is not Found."}, 400
    #     for item in items:
    #         if item['id'] == id:
    #             item['item']['name'] = request_data['name']
    #             item['item']['price'] = request_data['price']
    #         return {"Message": "Item updated successfully"}, 200
    #     return {"Message": "Item not found"}, 404
    
    # @blp.arguments(ItemSchema)
    # def post(self, request_data):
    #     item  = {
    #         "id" :uuid.uuid4().hex,
    #         "item": {
    #             "name": request_data['name'],
    #             "price": request_data['price']
    #         }
    #     }
    #     items.append(item)     
    #     return {"Message": "Item added successfully"}, 201
    

    # def delete(self):
    #     id = request.args.get('id')
    #     if id == None:
    #         return {"Message": "Given ID is not Found."}, 404
    #     for item in items:
    #         if item['id'] == id:
    #             items.remove(item)
    #             return {"Message": "Item deleted successfully"}, 200
    #     return {"Message": "Item not found"}, 404