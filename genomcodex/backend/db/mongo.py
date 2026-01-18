from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "Genesis"
COLLECTION_NAME = "Database"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
dna_collection = db[COLLECTION_NAME]
