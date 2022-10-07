from mongoengine import Document, EmailField, StringField, IntField, DateTimeField


class DocumentOrganisation(Document):
    code: str = StringField(required=True, max_length=10)
    name: str = StringField(required=True, max_length=50)
    description: str = StringField(max_length=500)

    def pre_save(cls, sender, document, **kwargs):
        print("Pre Save of DocumentOrganisation: %s" % document.name)
