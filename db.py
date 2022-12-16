from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv(".env")


db_connection = os.getenv("db_connection")

connection = MongoClient(db_connection)

client = connection["instagram"]

def get_db(db_name:str="sessions"):
    db = client[db_name]
    return db