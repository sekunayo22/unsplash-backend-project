from fastapi import FastAPI
from fastapi_restful import Api
from src.api.routes.collections import Collections, CollectionPhotos
from src.api.routes.photos import Photos

def create_app():
    """Add resources and route path"""
    app = FastAPI()
    api = Api(app)

    api.add_resource(Collections(), "/collections")
    api.add_resource(CollectionPhotos(), "/collection-photos")
    api.add_resource(Photos(), "/photos" )

    return app


app = create_app()