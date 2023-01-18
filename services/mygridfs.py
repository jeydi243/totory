import os
import gridfs
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def connect():
    try:
        conn = MongoClient(host="127.0.0.1", port=27017)
        return conn[os.environ.get('DB_NAME_DEV')]
    except Exception as e:
        print(e)


db = connect()
gfs = gridfs.GridFS(db)
