from datetime import datetime
from bson import ObjectId
from fastapi.exceptions import ValidationException
from dtos.org_dto import OrganizationDTO
from schemas.organization import Organization
from mongoengine import DoesNotExist
from rich import print
import traceback


class OrgService:
    def registerOrg(self, organization: OrganizationDTO):
        try:
            # print(organization)
            print(f"Type of organization={type(organization)}")
            print(f"Type of active_date={type(organization.active_date)}")
            organization.active_date = datetime.fromisoformat(
                str(organization.active_date)
            )

            # print(datetime.fromisoformat(organization.active_date))
            org = Organization(**dict(organization)).save()
            print(f"The Organization was added successfully with id {org.id}")
            return org
        except BaseException as e:
            print(e)
            return {"erreur": e}

    def is_valid_iso_format(self, date_string: str) -> bool:
        try:
            # Attempt to parse the date string
            if it is not None:
                datetime.fromisoformat(date_string.replace("Z", "+00:00"))
                return True
        except ValueError:
            return False

    def getOrgs(self):
        try:
            json_test = [doc.__dict__() for doc in Organization.objects()]
            # print(f"Ici2 = {json_test}")
            return json_test
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"An unknown error occured = {e}")

    def deleteOrg(self, id: str):
        try:
            org = Organization.objects.get(id=id)
            org.delete()
            return f"Organization with {id=} deleted."
        except DoesNotExist as e:
            print(f"Organization with {id=}, does not exist.")

    def getOrganizationByLookups(self, lookups_id: str):
        return []

    def getOrganizationByParent(self, org_parent_id: str):
        try:
            json_results = [
                doc.__dict__()
                for doc in Organization.objects(
                    organization_parent_id=ObjectId(org_parent_id)
                )
            ]
            print(f"Found {len(json_results)} organizations")
            return json_results
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"An unknown error occured = {e}")

    def updateOrganization(self, updatedOrg: OrganizationDTO):
        try:
            print(f"Update Organization with ID={updatedOrg.id}")
            org_found = Organization.objects.get(id=ObjectId(updatedOrg.id))
            for key, value in dict(updatedOrg).items():
                if "date" in key and self.is_valid_iso_format(value):
                    org_found[key] = datetime.fromisoformat(value)
                    if not isinstance(org_found[key], datetime):
                        raise ConvertDateException(
                            f"la convertion de la date fournis {updatedOrg.model_dump()[key]} en str vers datetime n'a pas marché"
                        )
                    print(f"Update key={key} by value='{value}'")
                elif key == "lookups_id" and self.is_valid_objectid(value) == True:
                    org_found[key] = value

            org_found.save()

        except ValidationException as e:
            print(f"An ValidationException occurred {e} ")
        except BaseException as e:
            print(f"An exception occurred {e} ")
            stacktrace = traceback.format_exc()
            print(stacktrace)


class ConvertDateException(Exception):
    pass
