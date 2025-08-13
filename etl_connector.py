from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
RIOT_COLLECTION = os.getenv("RIOT")

if not all([MONGO_URI, COLLECTION_NAME, RIOT_COLLECTION]):
    raise ValueError("Missing one or more required environment variables.")

client = MongoClient(MONGO_URI)
db = client[COLLECTION_NAME]
riot = db[RIOT_COLLECTION]

def save_result(ip, data):
    riot.insert_one({"ip": ip, "result": data})