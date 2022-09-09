from dtos.org_dto import OrgDTO
from schemas.organization import Organization


class OrgService:
    def create(self, organization: OrgDTO):
        try:
            org = Organization(**organization.dict()).save()
            return org
        except BaseException as e:
            print(e)