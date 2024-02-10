from fastapi_restful import Resource, set_responses
from src.api.controllers.collection_controller import CollectionController
from src.api.schema.collection_schema import CollectionSchema

class Collections(Resource):
    def __init__(self) -> None:
        pass

    def get(self):
        response = CollectionController().get_collections()
        return response 
    
    def put(self, collection_id: str, photo_id: str):
        response = CollectionController().add_to_collection(collection_id=collection_id, photo_id=photo_id)
        return response
    
    def post(self, photo_id: str):
        response = CollectionController().download_photo(photo_id=photo_id)
        return response


class CollectionPhotos(Resource):
    def __init__(self) -> None:
        pass

    def get(self, collection_id: str):
        response = CollectionController().get_collection_photos(collection_id=collection_id)
        return response