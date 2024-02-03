from fastapi_restful import Resource


class Collections(Resource):
    def get(self):
        return "done"
    
    def post(self):
        return "done"
    