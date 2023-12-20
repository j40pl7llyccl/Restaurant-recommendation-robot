# database.py
import pymongo
import config

def get_mongo_connection():
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING, 27017)
    return client[MONGO_DB_NAME]

def get_text_mining_news_collection():
    db = get_mongo_connection()
    return db.textMiningNews
