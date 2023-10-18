from mongoengine import Document, StringField, DateTimeField, FileField, ListField


class Resource(Document):
    file: any = FileField()
    filename: str = StringField()
    mimetype: str = StringField()
