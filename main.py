from concurrent.futures import process
from fastapi import FastAPI
import motor.motor_asyncio
import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ)

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI_DEV"])
db = client.college


@app.get("/")
async def root():
    return {"message": "Hello World"}
