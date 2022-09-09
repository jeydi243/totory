

class OrgService:
    
    def create(self,organization:OrgDTO):
        org = organization(**organization.dict()).save()
        
        return org
        