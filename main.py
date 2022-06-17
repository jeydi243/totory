from dotenv import load_dotenv
from fastapi import FastAPI, Form, UploadFile, File
from rich import print
import uvicorn
import json
import os
import motor.motor_asyncio
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse
from models.employee import EmployeeDTO


load_dotenv()

app = FastAPI()
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI_DEV"])
@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    exc_json = json.loads(exc.json())
    response = {"message": [], "data": None}

    for error in exc_json:
        response["message"].append(error["loc"][-1] + f": {error['msg']}")

    return JSONResponse(response, status_code=422)


@app.post("/management/employees")
async def add_employee(
    cover_letter: str = Form(...),
    resume_file: UploadFile = File(...),
    school_diploma_file: UploadFile = File(...),
    profile_img: UploadFile = File(...),
):
    print(resume_file.filename)
    print(school_diploma_file.filename)
    print(profile_img.filename)
    return {"message": cover_letter}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)
