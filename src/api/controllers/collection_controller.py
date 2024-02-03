import src.utils.config  as config

class CollectionController():
    """Collection Controller"""
    def __init__(self):
        """collection controller constructor"""
        pass

    def get_collections(self, keyword: str):
        """Get collections"""
        result = config.api.search.collections(keyword)
        return result
    def get_collection_photos(self):
        """Get collection photos"""

