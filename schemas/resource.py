from mongoengine import Document, StringField, DateTimeField, FileField, ListField
from datetime import datetime

class Resource(Document):
    file: any = FileField()
    filename: str = StringField()
    mimetype: str = StringField()
