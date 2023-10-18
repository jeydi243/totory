from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, FileField


class ServiceRequest(Document):
    cover_letter = StringField(required=True, min_length=10, max_length=1000)
    request_date = DateTimeField(required=True, default=datetime.now())
    profile_img = FileField(required=True)
    org_id: str = StringField(require=False)
