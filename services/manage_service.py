from dtos.org_dto import OrgDTO
from schemas.organization import Organization
from mongoengine import DoesNotExist


class ManageService:
    def registerOrg(self, organization: OrgDTO):
        try:
            org = Organization(**dict(organization)).save()
            return org
        except BaseException as e:
            print(e)
            return {"erreur": e}

    def getOrgs(self):
        try:
            return Organization.objects.to_json()
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"{e}")

    def deleteOrg(self, id: str):
        try:
            org = Organization.objects.get(id=id)
            org.delete()
            return f"Organization with {id=} deleted."
        except DoesNotExist as e:
            print(f"Organization with {id=}, does not exist.")

    def updateOrg(self, updatedOrg: dict):
        try:
            up = 1
        except BaseException as e:
            print(e)
