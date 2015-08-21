import json
import os
import collections
from collections import OrderedDict
from bson import json_util
from flask import Flask
from flask import render_template, request, redirect, url_for, send_from_directory
from pymongo import MongoClient
from flask.ext.cors import CORS
from SimpleMapReduce import MapReduce
from multiprocessing.dummy import Pool as ThreadPool

app = Flask(__name__)
cors = CORS(app)
app.debug = True
port = 0
client = MongoClient('mongodb://simnyatsanga:godbless123@ds053310.mongolab.com:53310/heroku_v4m11b98')
db = client.heroku_v4m11b98
# client = MongoClient()
# db = client.restaurantdb

mapreduce = MapReduce()

def to_json(obj):
    return json.dumps(obj, default=json_util.default)

def to_raw_dict(cursor):
    collection = []

    pool = ThreadPool(4)

    for item in cursor:
        collection.append(item)

#TODO: Find best place to put mapreduce calls
    map_reduced = pool.map(mapreduce.map, collection, chunksize=4)
    pool.close()
    pool.join()

    # map_reduced = mapreduce.map(collection)
    sorted_result = mapreduce.sort(map_reduced)

#TODO:Find better way to get the first 10 elements
    top10_collection = []
    for restaurant in sorted_result[:50]:
        top10_collection.append(restaurant)
    return top10_collection

@app.route('/')
def retrieve_planets():
    # restaurant_collection = db.restaurants.find({"$and": [{'grades': {"$ne":[]} }, {'name':{"$ne":""}}]})

    # return to_json(to_raw_dict(restaurant_collection))
    return render_template('index.html', port=port)

@app.route('/top_10_restaurants')
def retrieve_best_restaurants():
    restaurant_collection = db.restaurants.find({"$and": [{'grades': {"$ne":[]} }, {'name':{"$ne":""}}]})

    return to_json(to_raw_dict(restaurant_collection))


@app.route('/by_cuisine/<cuisine>')
def retrieve_by_cuisine(cuisine):
    restaurant_collection = db.restaurants.find({"$and": [{'grades': {"$ne":[]} }, {'name':{"$ne":""}}, {"cuisine":{"$eq":cuisine}}]})
    return to_json(to_raw_dict(restaurant_collection))

@app.route('/by_borough/<borough>')
def retrieve_by_borough(borough):
    restaurant_collection = db.restaurants.find({"$and": [{'grades': {"$ne":[]} }, {'name':{"$ne":""}}, {"borough":{"$eq":borough}}]})
    return to_json(to_raw_dict(restaurant_collection))

# def pass_port_to_js(port):
#     return render_template('index.html', port=port)

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # pass_port_to_js(port)
