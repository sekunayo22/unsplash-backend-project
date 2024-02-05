from fastapi_restful import Resource, set_responses
from src.api.controllers.collection_controller import CollectionController
from src.api.schema.collection_schema import CollectionSchema

class Collections(Resource):
    def __init__(self) -> None:
        pass

    def get(self):
        response = CollectionController().get_collections()
        return response 

class CollectionPhotos(Resource):
    def __init__(self) -> None:
        pass

    def get(self, keyword: str):
        response = CollectionController().get_collection_photos(keyword=keyword)
        return response