from pymongo import MongoClient
import gridfs


db = MongoClient("localhost", 27017)["gesi-developement"]
fs = gridfs.GridFS(db)
