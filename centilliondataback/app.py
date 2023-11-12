from centilliondataback import app
from pymongo import MongoClient
from fastapi.responses import JSONResponse
from bson import json_util
import json
import pandas as pd


client = MongoClient('mongodb://db:27017/')
db = client['driverhero']

# @app.get('/')
# def index():
#     return db.list_collection_names()

@app.get('/{collection_name}')
def get_all(collection_name):
    collection = db[collection_name]
    return  json.loads(json_util.dumps([doc for doc in collection.find({})]))



# @app.get('/insert_data')
# def insert_data():
#     collection = db['leads_de']
#     # Read the data
#     df = pd.read_csv('./4.csv')
#     df = df.to_dict('records')
#     # Insert the data
#     collection.insert_many(df)
#     return  {'status': 'success'}


# @app.get('/delete_data')
# def delete_data():
#     collection = db['leads_de']
#     collection.delete_many({})
#     return  {'status': 'success'}