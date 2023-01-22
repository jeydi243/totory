import os
import json
import uvicorn
import asyncio
from rich import print
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form, File
from controllers import teachers, students, employees, users, docs, courses, resources

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect


load_dotenv()
connect(db=os.environ["DB_NAME_DEV"], host="localhost", port=27017)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(docs.router)
app.include_router(users.router)
app.include_router(students.router)
app.include_router(resources.router)
app.include_router(courses.router)
app.include_router(teachers.router)
app.include_router(employees.router)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc):
    print(f"Invalid data sent: {exc}, {request}")
    exc_json = json.loads(exc.json())
    response = {"message": [], "data": None}

    for error in exc_json:
        response["message"].append(error["loc"][0] + error["msg"])

    return JSONResponse(response, status_code=422)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4000)
