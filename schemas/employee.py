from datetime import datetime

from mongoengine import DateTimeField, DictField, FileField, ListField, StringField

from schemas.person import Person


class Employee(Person):
    position: list = ListField(StringField(required=True))
    biography = StringField(required=True, min_length=20, max_length=500)
    educations = ListField(DictField(required=True))
    onboarding = ListField(DictField(required=False))
    experiences = ListField(DictField(required=True))
    domain: str | list = StringField(required=True)

    cover_letter = StringField(required=True, min_length=10, max_length=1000)
    hire_date = DateTimeField(required=True, default=datetime.now())
    resume_file = FileField(required=True)
    profile_img = FileField(required=True)
    org_id: str = StringField(require=False)

    def __dict__(self):
        return {"position": self.position, "resume_file": self.resume_file, "experiences": self.experiences, "profile_img": self.profile_img}

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
        orm_mode = True

    # # init class
    # def __init__(self, **args):
    #     super().__init__(**args)
