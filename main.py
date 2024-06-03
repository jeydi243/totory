import os
import json
import uvicorn
import asyncio
from rich import print
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request, UploadFile, File
from controllers import teachers_controller, students_controller, employees_controller, classes_controller, docs_controller, services_controller, lookups_controller, users_controller
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from fastapi.responses import JSONResponse
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
app.include_router(students_controller.router)
app.include_router(users_controller.router)
app.include_router(teachers_controller.router)
app.include_router(employees_controller.router)
app.include_router(classes_controller.router)
app.include_router(lookups_controller.router)
app.include_router(docs_controller.router)
app.include_router(services_controller.router)


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
    uvicorn.run(app, host="0.0.0.0", port=4000)
