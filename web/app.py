from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert_one({
    "num_users":0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]["num_users"]
        new_num = prev_num + 1
        UserNum.update_one({}, {"$set": {"num_users":new_num}})
        return str("Olá Usuário"+ str(new_num))


def Checkposted(postedData, Function):
    if (Function == "add" or Function == "sub" or Function == "multiply"):
        if "x" not in  postedData or "y" not in postedData:
            return 301
        else:
            return 200
    else:
        if (Function == "division"):
            if "x" not in postedData or "y" not in postedData:
                return 301
            elif int(postedData["y"]) == 0:
                return 302
            else:
                return 200
            

class Add(Resource):
    def post(__self__):

        # data posted
        postedData = request.get_json()

        #validation params
        status_code = Checkposted(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "Error",
                "Status Code": status_code
            }
            return jsonify(retJson)
        

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap={
            'Message': ret,
            'status Code': status_code
        }
    
        return jsonify(retMap)
    

class Sub(Resource):
    def post(__self__):

        # data posted
        postedData = request.get_json()

        #validation params
        status_code = Checkposted(postedData, "sub")
        if (status_code != 200):
            retJson = {
                "Message": "Error",
                "Status Code": status_code
            }
            return jsonify(retJson)
        

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x-y
        retMap={
            'Message': ret,
            'status Code': status_code
        }
    
        return jsonify(retMap)
    

class Multiply(Resource):
    def post(__self__):

        # data posted
        postedData = request.get_json()

        #validation params
        status_code = Checkposted(postedData, "multiply")
        if (status_code != 200):
            retJson = {
                "Message": "Error",
                "Status Code": status_code
            }
            return jsonify(retJson)
        

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x*y
        retMap={
            'Message': ret,
            'status Code': status_code
        }
    
        return jsonify(retMap)

class Divide(Resource):
    def post(__self__):

        # data posted
        postedData = request.get_json()

        #validation params
        status_code = Checkposted(postedData, "division")
        if (status_code != 200):
            retJson = {
                "Message": "Error",
                "Status Code": status_code
            }
            return jsonify(retJson)
        

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = (x*1.0)/y
        retMap={
            'Message': ret,
            'status Code': status_code
        }
    
        return jsonify(retMap)






api.add_resource(Add, "/add")
api.add_resource(Sub, "/sub")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")
api.add_resource(Visit, "/hello")


@app.route('/')
def HelloWord():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

