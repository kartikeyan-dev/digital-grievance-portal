from pymongo import MongoClient

SECRET_KEY = "secret123"
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "grievance_portal"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

complaints_collection = db["complaints"]