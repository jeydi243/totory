from dtos.org_dto import OrgDTO
from schemas.organization import Organization


class ManageService:
    def registerOrg(self, organization: OrgDTO):
        try:
            org = Organization(**organization.dict()).save()
            return org
        except BaseException as e:
            print(e)

    def getOrgs(self):
        try:
            return Organization.objects.to_json()
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"{e}")
