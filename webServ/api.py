from flask import Flask, jsonify
import pymongo
import sys
sys.path.append('..')
from mongoconection import client, my_db, my_collection
import json
""" This module is for manage the web service with flask,
    the only function is redirect and start the search by
    a pokemon name and get the info available in the DB """


app = Flask(__name__)

@app.route("/")
def homePage():
    try:
        # namePoke = input('Enter the Pokemon name to search: ')
        # consulta(namePoke)
        confirm = "You are now conected to the server,\n\nplease type in your url box the Pokemon's name to search it:\n\t"
        confirm2 = "i.e,\n\t\tlocalhost:5000/bulbasaur\n\tfor search bulbasaur's info"
        return confirm + confirm2
    except:
        return "Server error"

@app.route("/<name>", methods=['GET'])
def consulta(name):
    try:
        consResult = []
        my_cursor = my_collection.find({
            "name": name
        })

        for item in my_cursor:
            # print(item)
            consResult.append(item)
        # print(consResult)
        del consResult[0]['_id']
        # print(consResult)
        return jsonify(consResult)
    except:
        return "Data not found, try again"

if __name__ == "__main__":
    app.run()
