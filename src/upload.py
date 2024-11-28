from pymongo.mongo_client import MongoClient
import json
from constant.__init__ import *
import pandas as pd


client = MongoClient(MONGO_DB_URL)
df = pd.read_csv("notebooks\wafer_23012020_041211.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
json_record = list(json.loads(df.T.to_json()).values())
client[MONGO_DATABASE_NAME][MONGO_COLLECTION_NAME].insert_many(json_record)