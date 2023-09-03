import os
import json
import uvicorn
import asyncio
from rich import print
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form, File
from controllers import classes_controller, contents_controller, docs_controller, employees_controller, resources_controller, lookups_controller, students_controller, users_controller
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, ValidationException
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
app.include_router(docs_controller.router)
app.include_router(users_controller.router)
app.include_router(students_controller.router)
app.include_router(resources_controller.router)
app.include_router(contents_controller.router)
app.include_router(classes_controller.router)
app.include_router(lookups_controller.router)
app.include_router(employees_controller.router)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"Invalid data sent: {exc.errors()}, {request.body}")
    exc_json = exc.errors()
    response = {"message": [], "data": None}

    for error in exc_json:
        response["message"].append(error["loc"][1] + " " + error["msg"])

    return JSONResponse(response, status_code=422)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4000)
