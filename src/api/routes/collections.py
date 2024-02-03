from fastapi_restful import Resource, set_responses
from src.api.controllers.collection_controller import CollectionController
from src.api.schema.collection_schema import CollectionsSchema

class Collections(Resource):
    def __init__(self) -> None:
        pass

    def get(self, keyword: str):
        response = CollectionController().get_collections(keyword="office")
        return list(CollectionsSchema(**response))

class CollectionPhotos(Resource):
    def __init__(self) -> None:
        pass

    def get(self):
        CollectionController().get_collection_photos()