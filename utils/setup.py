import pymongo
import os


def setup_Mongo():
    if os.getenv("MongoDB"):
        connection_string="mongodb+srv://" + os.getenv("Mongo_UserName") +':'+ os.getenv("Mongo_Password")+'@'+os.getenv("MongoDB")
        client = pymongo.MongoClient(connection_string)
    else:
        client = pymongo.MongoClient('localhost', 27017)
    return client