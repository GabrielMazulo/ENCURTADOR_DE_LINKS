from ninja import Router
from .shemas import LinksSchemas

shortner_router = Router()

@shortner_router.post('create/')
def create(request, link_shema: LinksSchemas):
    print(link_shema.dict())
    return {'Status': 'OK'}


