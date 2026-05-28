import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY", "secret123")

client = MongoClient(MONGO_URI)
db = client["grievance_portal"]

complaints = db["complaints"]