from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client[os.getenv("COLLECTION_NAME")]
riot = db[os.getenv("RIOT")]

def save_result(data):
    riot.insert_one(data)