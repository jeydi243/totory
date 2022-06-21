from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request, UploadFile, File
from rich import print
from rich import print
import uvicorn
import json
import os
import shutil
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi.responses import JSONResponse
from models.employee import EmployeeDTO


load_dotenv()

app = FastAPI()
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URI_DEV"])
@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc):
    print(f"The client sent invalid data!: {exc}")
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

    print(resume_file.content_type)
    print(school_diploma_file.content_type)
    print(profile_img.content_type)

    try:
        path_to_store = store_path("resume_file",ext, "employees", "fd1452fvd")
        with open(path_to_store, "wb") as buffer:
            shutil.copyfileobj(resume_file.file, buffer)

        path_to_store = store_path("diploma_file",ext, "employees", "fd1452fvd")
        with open(path_to_store, "wb") as buffer:
            shutil.copyfileobj(school_diploma_file.file, buffer)

        path_to_store = store_path("profile_picture", "employees", "fd1452fvd")
        with open(path_to_store, "wb") as buffer:
            shutil.copyfileobj(profile_img.file, buffer)
    except FileNotFoundError as ffe:
        print(ffe)

    return {"message": cover_letter}


def store_path(filename: str,ext:str, model: str, id: str) -> str:
    # return current word directory cwd
    to_create = os.path.join(os.getcwd(), "STORAGES")
    if not os.path.exists(to_create):
        os.mkdir(to_create)
        print("STORAGES directory created")
        to_create = os.path.join(to_create, model.upper())
    if not os.path.exists(to_create):
        os.mkdir(to_create)
        print(f"{model.upper()} directory created")
        to_create = os.path.join(to_create, id)
    if not os.path.exists(to_create):
        os.mkdir(to_create)
    return os.path.join(to_create, filename)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)
