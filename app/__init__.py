from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["MONGODB_URI"]
mongo = PyMongo(app)

@app.route("/")
def index():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
