import os
import json
import uvicorn
import logging
from rich import print
from dotenv import load_dotenv
from fastapi import FastAPI, Request, status
from pydantic import ValidationError
from mongoengine import connect
from controllers import teachers_controller, students_controller, employees_controller, classes_controller, docs_controller, services_controller, lookups_controller, users_controller, org_controller
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

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
app.include_router(org_controller.router)


# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("custom_logger")

handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Middleware to log request details including query parameters
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        query_params = dict(request.query_params)
        logger.info(f"Request: {request.method} {request.url} | Query: {query_params}")
        response = await call_next(request)
        return response

# Nice to have custom logging
# app.add_middleware(LoggingMiddleware)

@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(exc.errors())
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    ) 


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)
