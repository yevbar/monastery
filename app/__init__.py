from bson.json_util import dumps
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from json import loads
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["MONGODB_URI"]
mongo = PyMongo(app)

"""
Root url, will be home page
"""
@app.route("/")
def index():
    return "Hello from Flask!"

"""
Database test, pass in /database?val=VALUE

Functionality: Takes in val argument, appends to collection, and returns entire collection
"""
@app.route("/database")
def database_test():
   args = request.args
   val = args["val"]
   mongo.db.vals.insert_one({
       "val": val
    })
   vals = mongo.db["vals"]
   cursor = vals.find({})
   return jsonify({"vals": loads(dumps(cursor))}) 

if __name__ == "__main__":
    app.run(host="0.0.0.0")
