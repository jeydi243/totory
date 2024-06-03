from datetime import datetime
from typing import List
from mongoengine import Document, StringField, DateTimeField, FileField, ListField
from schemas.resource import Resource
from datetime import datetime

class ServiceRequest(Document):
    cover_letter = StringField(required=True, min_length=10, max_length=1000)
    request_date: datetime = DateTimeField(required=True, default=datetime.now())
    completion_date: datetime = DateTimeField(required=True)
    student_id: str = StringField(required=True)
    service_id: str = StringField(require=False)
    request_status: str = StringField(require=False)
    attachements: List[str] = ListField(Resource)
    attachements2: List[str] = ListField(FileField())
    
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")
