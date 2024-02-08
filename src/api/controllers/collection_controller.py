import src.utils.config  as config
from src.api.schema.collection_schema import CollectionSchema
from unsplash import UnsplashError, UnsplashAuthError

class CollectionController():
    """Collection Controller"""
    def __init__(self):
        """collection controller constructor"""
        pass

    def get_collections(self) -> list[CollectionSchema]:
        """Get collections"""
        value_array = []
        result = []
        try:
            result = config.api.collection.all(2, 10)
        except UnsplashAuthError as unsplashauthexception:
            raise unsplashauthexception
        except UnsplashError as unsplashexception:
            raise unsplashexception
        except Exception as exc:
            raise exc
        for item in result:
            value = {}
            value["title"] = item.title
            value["total_photos"] = item.total_photos
            value["cover_photo"] = item.cover_photo.urls.raw
            value_array.append(value)
        return value_array
    
    def get_collection_photos(self, keyword: str):
        """Get collection photos"""
        value_array = []
        result = []
        try:
            result = config.api.collection.all(2, 10)
        except UnsplashAuthError as unsplashauthexception:
            raise unsplashauthexception
        except UnsplashError as unsplashexception:
            raise unsplashexception
        except Exception as exc:
            raise exc
        for item in result:
            value = {}
            value["title"] = item.title
            value["total_photos"] = item.total_photos
            value["cover_photo"] = item.cover_photo.links.self
            value_array.append(value)
        return value_array