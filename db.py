from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client[os.getenv("COLLECTION_NAME")]
riot = db[os.getenv("RIOT")]

def save_result(ip, data):
    riot.insert_one({"ip": ip, "result": data})