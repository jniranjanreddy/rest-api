from flask import Flask, request
from microblog 


blog_blp = Blueprint("login", __name__, description="Operations on Items")


@blp.route('/item')
class Item(MethodView):
    
    @blp.response(200, ItemGetSchema(many=True))
    def get(self):
        id = request.args.get('id')
        if id is None:
            return items
        try:
            for item in items:
                if item['id'] == id:
                    return [item]
        except KeyError:
            abort(message="Record Doesn't Exist.")