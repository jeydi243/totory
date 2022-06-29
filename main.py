from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request, UploadFile, File
from rich import print
from controllers.employees import router as router_employee
from controllers.students import router as router_students
from controllers.teachers import router as router_teachers
import uvicorn
import json
import os

from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse
from dtos.employee import EmployeeDTO
from mongoengine import connect


load_dotenv()
connect(db="gesi-development", host="localhost", port=27017)

app = FastAPI()
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI_DEV"])
@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc):
    print(f"The client sent invalid data!: {exc}, {request}")
    exc_json = json.loads(exc.json())
    response = {"message": [], "data": None}

    for error in exc_json:
        response["message"].append(error["loc"][-1] + f": {error['msg']}")

    return JSONResponse(response, status_code=422)


app.include_router(router_employee)
app.include_router(router_students)
app.include_router(router_teachers)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)
