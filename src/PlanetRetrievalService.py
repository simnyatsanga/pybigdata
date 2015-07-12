import json
import collections
from collections import OrderedDict
from bson import json_util
from flask import Flask
from pymongo import MongoClient
from flask.ext.cors import CORS
from SimpleMapReduce import MapReduce

app = Flask(__name__)
cors = CORS(app)
app.debug = True
client = MongoClient()
db = client.restaurantdb

mapreduce = MapReduce()

def to_json(obj):
    return json.dumps(obj, default=json_util.default)

def to_raw_dict(cursor):
    collection = []

    for item in cursor:
        collection.append(item)

#TODO: Find best place to put mapreduce calls
    mapped = mapreduce.map(collection)
    reduced = mapreduce.reduce(mapped)
    sorted_result = mapreduce.sort(reduced)

#TODO:Find better way to get the first 10 elements
    x = 0
    top10_collection = {}
    for restaurant_name, restaurant_grade in (sorted_result.iteritems()):
        if x < 10:
            top10_collection[restaurant_name] = restaurant_grade
            x = x + 1
        else:
            break
#TODO:Sorting twice: in mapreduce and here, not good
    return OrderedDict(sorted(top10_collection.items() , key=lambda restaurant: restaurant[1], reverse=True))

@app.route("/")
def retrieve_planets():
    restaurant_collection = db.restaurants.find({"$and": [{'grades': {"$ne":[]} }, {'name':{"$ne":""}}]})

    return to_json(to_raw_dict(restaurant_collection))

if __name__ == "__main__":
    app.run()
