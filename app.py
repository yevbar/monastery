from bson.json_util import dumps
from flask import Flask, jsonify, request, send_from_directory
from flask_pymongo import PyMongo
from json import loads
import nltk
import os

from stat_parser import Parser

application = Flask(__name__, static_folder='./react_app/build')
application.config["MONGO_URI"] = os.environ["MONGODB_URI"]
mongo = PyMongo(application)

@application.route("/hello")
def hello():
    return "hello"

"""
+ Take string (question)
- Convert string to query
- Run query on database
- Get most relevant answer
- Return most relevant answer
^ should also return link of resource for credibility sake
"""

"""
- Take blogpost
- Pluck out important statements from blogpost
https://github.com/miso-belica/sumy
% for each %
- Construct statement object with tags and features of statment
- Insert statement
"""

"""
For demo - find a question that is substantial but not asked/answered on Quora, answer it in front of them
"""

"""
Query through mongo for terms question etc
scrae
"""

def query_database(query):
    # TODO, incorporate query["rest"] in some way that helps with refining search?
    # The following line says that we need one of the following: question, action, topic (affected_entity)
    similar_statements = mongo.db.statements.find({ $or: [{"question": query["question"]}, {"action": query["action"]}, {"affected_entity": query["affected_entity"]}]})
    print(similar_statements)
    return query

def string_to_query(string):
    parser = Parser()
    parsed = parser.parse(string)
    question = []
    question.extend([word for word,pos in parsed.pos() if pos=='WP' or pos=='WRB'])
    action = []
    action.extend([word for word,pos in parsed.pos() if 'VB' in pos])
    affected_entity = []
    affected_entity.extend([word for word,pos in parsed.pos() if 'NN' in pos])
    particle = list(parsed.subtrees(filter=lambda x: x.label()=='PRT'))
    tree = parsed
    verb_phrases_list = list(parsed.subtrees(filter=lambda x: "V" in x.label()))[0]
    entity = [x for x in parsed.pos() if x[0] == affected_entity[0]][0]
    print(question)
    print(action)
    print(affected_entity)
    print(parsed.pos()[parsed.pos().index(entity)+1:])
    output = {
        "question": question,
        "action": action,
        "affected_entity": affected_entity,
        "rest": parsed.pos()[parsed.pos().index(entity)+1:]
    }
    return output

@application.route("/question", methods=["POST"])
def question():
    inbound_data = request.get_json()
    question = inbound_data["question"]
    query = string_to_query(question)
    result = query_database(query)
    return jsonify({"answer": str(result)})

# Serve React App
@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("./react_app/build/" + path):
        return send_from_directory('./react_app/build', path)
    else:
        return send_from_directory('./react_app/build', 'index.html')

"""
Database test, pass in /database?val=VALUE

Functionality: Takes in val argument, appends to collection, and returns entire collection
"""
@application.route("/database")
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
    application.run(host="0.0.0.0")
