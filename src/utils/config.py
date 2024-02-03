import os
from unsplash import Api, Auth
from dotenv import load_dotenv

load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")

auth = Auth(client_id, client_secret, redirect_uri)
api = Api(auth)




