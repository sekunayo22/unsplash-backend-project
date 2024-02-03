from src.api.schema.photo_schema import PhotoSchema

class CollectionsSchema():
    """"""
    def __init__(self):
        pass
    title: str
    total_photos: int
    photos: list(PhotoSchema)
