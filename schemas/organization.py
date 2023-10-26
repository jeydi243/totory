from mongoengine import Document, EmailField, StringField, ReferenceField
import mongoengine


class Organization(Document):
    code: str = StringField(require=True)
    name: str = StringField(require=True)
    description: str = StringField()
    organization_parent_id: str = ReferenceField("self", reverse_delete_rule=mongoengine.NULLIFY)

    meta = {"strict": False}
