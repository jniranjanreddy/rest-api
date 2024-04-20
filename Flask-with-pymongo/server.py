from flask import Flask, request, Response
import pymongo
import json
from pymongo import MongoClient
from bson import ObjectId
app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.company
    mongo.server_info() # Trigger exeption if cannot connect to the database
except: 
    print("Error connecting to database")
##########################################
##Get method
@app.route('/students', methods=['GET'])
def get_some_users():
    try:
        data = list(db.users.find())
        print(data)
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response=json.dumps(data),
            status=500,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"Cannot read users"}),
            status=500,
            mimetype="application/json"
        )

##########################################
## Post Method
@app.route('/students', methods=['POST'])
def create_user():
    try:
        user = {
            "name":request.form["name"],
            # "lastname":request.form["lastname"]
        }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response=json.dumps(
                {"message":"user created", 
                 "id":f"{dbResponse.inserted_id}"
                }
            ),
            status=200,
            mimetype="application/json"
         )
    except Exception as ex:
        print("*******")
        print(ex)
        print("*******")
#########################################
## Put Method
@app.route('/students/<id>', methods=['PATCH'])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"name":request.form["name"]}},
            # {"$set":{"lastname":request.form["lastname"]}}
        )
        # print(dbResponse.modified_count)
        # for attr in dir(dbResponse):
        #     print(f"*****{attr}*****")
        if dbResponse.modified_count == 1:
           return Response(
               response=json.dumps(
                   {"message":"user updated", 
                    "id":f"{id}"
                   }
               ),
               status=200,
               mimetype="application/json"
            )
        return Response(
            response=json.dumps(
                {"message":"Nothing to update", 
                 "id":f"{id}"
                }
            ),
            status=200,
            mimetype="application/json"
         )
    except Exception as ex:
        print("*******")
        print(ex)
        print("*******")
        return Response(
            response=json.dumps(
                {"message":"Cannot update user", 
                 "id":f"{id}"
                }
            ),
            status=500,
            mimetype="application/json"
         )
#########################################
## Delete Method
@app.route('/students/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id":ObjectId(id)})
        # for attr in dir(dbResponse):
        #     print(f"*****{attr}*****")
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps(
                    {"message":"user Deleted", 
                     "id":f"{id}"
                    }),
                status=500,
                mimetype="application/json"
            )
        return Response(
                response=json.dumps(
                    {"message":"user not found","id":f"{id}"}),status=500,mimetype="application/json")
    except Exception as ex:
        print("*******")
        print(ex)
        print("*******")
        return Response(
            response=json.dumps(
                {"message":"Sorry Cannot delete user","id":f"{id}"}),status=500,mimetype="application/json")
######################################

if __name__ == '__main__':
    app.run(port=80, debug=True)