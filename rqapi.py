from flask import Flask, request, jsonify, flash
import sqlite3
from rqdbase import * 

app = Flask(__name__)
app.config["DEBUG"] = True


testdata = [ {"quote":"quote1", "topic":"topic1" , "authors":["author1","author2"]},
{"quote":"quote2", "topic":"topic2" , "author":"author2"},
{"quote":"quote3", "topic":"topic3" , "author":"author3"},
{"quote":"quote4", "topic":"topic4" , "author":"author4"},
{"quote":"quote5", "topic":"topic5" , "author":"author5"}
]
testdata2 = {"content":"quote6", "topic":"topic6" , "author":"author6heeyoooo"}

@app.route("/")
def homepage():
    return "Welcome to Requote API"

@app.route("/quotes/all",methods=["GET"])
def allquotes():
    return jsonify(testdata)


@app.route("/add/quote",methods = ["POST"])
def addquote():
    request_data = request.get_json() # request a library which has get_json() method | request_data is a variable that I define to store the thing that get_json() method's serves
    # To see 'request_data's content | Remember it is a dictionary that converted from json to Python object (dict) by Flask 
    print(request_data["content"])
    print(request_data["topic"])
    print(request_data["author"])
    print(type(request_data)) # The type of request_data = 'dict'
    add_quote_db(request_data)
    return request_data["topic"],"Quote Added Successfuly"
    

@app.route("/delete/quote",methods = ["DELETE"])
def deletequote():
    request_data = request.get_json()
    print(request_data)
    print(type(request_data))
    id = request_data["id"]
    print(id)
    print(type(id))
    delete_quote_db(id)
    return str(request_data["id"])


@app.route("/update/quote",methods = ["UPDATE"])
def updatequote():
    pass






app.run()
