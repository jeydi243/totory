import os
from pathlib import Path
from shutil import copyfileobj
from os.path import join, exists
from fastapi import UploadFile


def store_path(id: str, model: str) -> str:
    to_create = join(os.getcwd(), "STORAGES", model, id)
    if not exists(to_create):
        try:
            Path(to_create).mkdir(parents=True)
        except e:
            print(e)
    return to_create


def process_file(file: UploadFile, filename: str, id: str, model: str):
    ext = "." + file.content_type.split("/")[1]
    path = store_path(id, model)
    with open(join(path, f"{filename}{ext}"), "wb") as buffer:
        copyfileobj(file.file, buffer)
