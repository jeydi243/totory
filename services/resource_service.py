from services.mygridfs import gfs
from gridfs.errors import NoFile


class ResourceService:
    def get(self) -> list[any]:
        # return gfs.find()
        data:list = []
        for out in gfs.list():
            data.append(out)
        return data

    def add(self, img: bytes):
        try:
            result = gfs.put(img)
            print(f"The result is {result}")
        except Exception as e:
            print(e)

    def get_resource_info(self, id: str):
        reponse = gfs.find_one({"file_id": id})
        return reponse if reponse is not None else "There is not file like this"

    def read_stream(self, id: str):
        return gfs.get({"file_id": id})._file

    def get_resource_file(self, id: str):
        try:
            return gfs.get(id)
        except NoFile as e:
            return f"No file with {id=}"
        
    def download_resource(self, id: str):
        try:
            return gfs.get(id)
        except NoFile as e:
            return f"No file with {id=}"
