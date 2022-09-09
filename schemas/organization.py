from mongoengine import Document, EmailField, StringField
from pkg_resources import require


class Organization(Document):
    code: str = StringField(require=True)
    name: str = StringField(require=True)
    description: str = StringField()
    organization_parent_id: str = StringField()

    meta = {"strict": False}
