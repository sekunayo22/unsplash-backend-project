from fastapi import FastAPI
from fastapi_restful import Api
from src.api.routes.collections import Collections, CollectionPhotos

def create_app():
    """Add resources and route path"""
    app = FastAPI()
    api = Api(app)

    api.add_resource(Collections(), "/collections")
    api.add_resource(CollectionPhotos(), "/collection-photos")

    return app


app = create_app()