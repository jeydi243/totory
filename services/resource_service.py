
from services.gridfs_service import fs as fss, bucket
from fastapi import UploadFile
from gridfs.grid_file import GridOutCursor, GridOut
from bson.objectid import ObjectId


class ResourceService:
    def getByID(self, id: str) -> list[any]:
        assert id is not None
        try:
            if id is not None:
                print(f"Find file with id {id}")
                file = fss.get(id)
                return file
            else:
                return {"message": "No file found"}
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"{e}")

    def get(self) -> list[dict]:
        reponse: list[dict] = []
        files: GridOutCursor = fss.find()
        file: GridOut
        for file in files:
            reponse.append(
                {
                    "id": str(file._id),
                    "filename": file.filename,
                    "metadata": file.metadata,
                    "upload_date": file.upload_date,
                    "content_type": file.content_type,
                }
            )
        return reponse

    def add(self, file: UploadFile) -> dict:
        try:
            reponse = fss.put(file.file, filename=file.filename, chunked=True)
            return {"message": f"The file was uploaded", "id": str(reponse)}
        except BaseException as e:
            print(f"Erreur lors du téléchargement {e}")
            return {"message": e}

    def deleteByID(self, id: str) -> dict | str:
        try:
            if fss.exists(ObjectId(id)):
                fss.delete(ObjectId(id))
                return f"The file with {id=}, was deleted"
            return f"Can't delete file with {id=} does not exist"

        except BaseException as e:
            print(f"An exception occurred {e.message}")

    def stream(self, id: str) -> bytes:
        try:
            out = bucket.open_download_stream(ObjectId(id))
            return out
        except fss.errors.NoFile as e:
            print(f"An exception occurred {e}")
            return f"No file with {id=}"
        
    def download(self, id: str) -> GridOut:
        try:
            out = fss.get(ObjectId(id))
            return out
        except fss.errors.NoFile as e:
            print(f"An exception occurred {e}")
            return f"No file with {id=}"
