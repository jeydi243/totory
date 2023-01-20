from pymongo import MongoClient
import gridfs


db = MongoClient("localhost", 27017)["gesi-development"]
fs = gridfs.GridFS(db)
