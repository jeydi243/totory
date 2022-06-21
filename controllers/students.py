from main import app

from fastapi import FastAPI, Form, Request, UploadFile, File


app = FastAPI()


@app.post("/students")
def add_student():
    return {"message": "Hello World"}


# all endpoint for model students
@app.get("/students")
def get_students():
    return {"message": "Hello World"}


@app.patch("/students")
def update_student():
    return {"message": "Hello World"}


@app.delete("/students")
def delete_student():
    return {"message": "Hello World"}
