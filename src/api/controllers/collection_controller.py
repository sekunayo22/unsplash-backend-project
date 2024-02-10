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
            value["id"] = item.id
            value["title"] = item.title
            value["total_photos"] = item.total_photos
            value["cover_photo"] = item.cover_photo.urls.raw
            value_array.append(value)
        return value_array
    
    def get_collection_photos(self, collection_id: str):
        """Get collection photos"""
        value_array = []
        result = []
        try:
            result = config.api.collection.photos(collection_id)
        except UnsplashAuthError as unsplashauthexception:
            raise unsplashauthexception
        except UnsplashError as unsplashexception:
            raise unsplashexception
        except Exception as exc:
            raise exc
        for item in result:
            value = {}
            value["lastName"] = item.user.last_name
            value["firstName"] = item.user.first_name
            value["publishedOn"] = item.user.updated_at
            value["profileImage"] = item.user.profile_image.small
            value["image"] = item.urls.raw
            value_array.append(value)
        return value_array
    
    def add_to_collection(self, collection_id: str, photo_id: str):
        """Add photo to collection"""
        result = []
        try:
            result = config.api.collection.add_photo(collection_id=collection_id, photo_id=photo_id)
        except UnsplashAuthError as unsplashauthexception:
            raise unsplashauthexception
        except UnsplashError as unsplashexception:
            raise unsplashexception
        except Exception as exc:
            raise exc
        return result
    
    def download_photo(self, photo_id: str):
        """Add photo to collection"""
        result = []
        try:
            result = config.api.photo.get(photo_id=photo_id)
        except UnsplashAuthError as unsplashauthexception:
            raise unsplashauthexception
        except UnsplashError as unsplashexception:
            raise unsplashexception
        except Exception as exc:
            raise exc 
        return result