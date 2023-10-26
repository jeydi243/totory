from dtos.content_dto import ContentDTO
from schemas.content import Content


class ContentService:
    def add_content(self, content: ContentDTO):
        co = Content(**content.dict()).save()
        print(f"add one content {co}")
        return co

    def getContents(self):
        try:
            val = Content.objects.values_list()
            print(val[0].to_json())
        except BaseException as e:
            print(e)

    def getById(self, id: str):
        return Content.objects.get(id=id)
