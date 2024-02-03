from fastapi_restful import Resource


class Photos(Resource):
    def get(self):
        return "done"