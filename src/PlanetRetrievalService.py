import json
from bson import json_util
from flask import Flask
from pymongo import MongoClient
from flask.ext.cors import CORS 

app = Flask(__name__)
cors = CORS(app)
app.debug = True
client = MongoClient()
db = client.restaurantdb

def to_json(obj):
    return json.dumps(obj, default=json_util.default)

def to_raw_dict(cursor):
    collection = []

    for item in cursor:
        collection.append(item)

    return collection

@app.route("/")
def retrieve_planets():
    restaurant_collection = db.restaurants.find()

    return to_json(to_raw_dict(restaurant_collection))

if __name__ == "__main__":
    app.run()
