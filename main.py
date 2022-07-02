import os
import json
import uvicorn
from rich import print
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request, UploadFile, File
from controllers import teachers, students, employees

from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse
from mongoengine import connect


load_dotenv()
connect(db=os.environ["DB_NAME_DEV"], host="localhost", port=27017)

app = FastAPI()

app.include_router(teachers.router)
app.include_router(students.router)
app.include_router(employees.router)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc):
    print(f"The client sent invalid data!: {exc}, {request}")
    exc_json = json.loads(exc.json())
    response = {"message": [], "data": None}

    for error in exc_json:
        response["message"].append(error["loc"][-1] + f": {error['msg']}")

    return JSONResponse(response, status_code=422)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)
