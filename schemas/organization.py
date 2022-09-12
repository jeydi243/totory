from mongoengine import Document, StringField


class Organization(Document):
    code: str = StringField(require=True)
    name: str = StringField(require=True)
    domain: str = StringField(require=True)
    description: str = StringField()
    organization_parent_id: str = StringField()

    meta = {"strict": False}
