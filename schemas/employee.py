from datetime import datetime
from mongoengine import StringField, FileField, DateTimeField, DictField, ListField

from schemas.person import Person


class Employee(Person):
    position = StringField(required=True)
    biography = StringField(required=True, min_length=20, max_length=500)
    educations = ListField(DictField(required=True))
    onboarding = ListField(DictField(required=False))
    experiences = ListField(DictField(required=True))
    domain = StringField(required=True)

    cover_letter = StringField(required=True, min_length=10, max_length=1000)
    hire_date = DateTimeField(required=True, default=datetime.now())
    resume_file = FileField(required=True)
    profile_img = FileField(required=True)
    org_id: str = StringField(require=False)
    
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        print("Pre Save: %s" % document.name)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print("Post Save: %s" % document.name)
        if "created" in kwargs:
            if kwargs["created"]:
                print("Created")
            else:
                print("Updated")

    class Config:
        from_attributes = True

    # # init class
    # def __init__(self, **args):
    #     super().__init__(**args)
