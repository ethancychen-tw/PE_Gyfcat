import requests
import json

class GfycatCaller(object):
    DEFAULT_API_ENDPOINT = 'https://api.gfycat.com/v1'
    TOKEN = None

    def __init__(self, client_id=None, client_secret=None, endpoint=DEFAULT_API_ENDPOINT):
        self.endpoint = endpoint
        self.client_id = client_id
        self.client_secret = client_secret


    def set_token(self):
        url = self.DEFAULT_API_ENDPOINT+"/oauth/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        resp = requests.post(url=url, data=json.dumps(data))
        if resp.status_code == 200:
            self.TOKEN = resp.json["access_token"]
        return self

    def get_trending(self, count=None):
        # no need for token
        url = self.DEFAULT_API_ENDPOINT + "/gfycats/trending"
        params = {}
        if count is not None:
            params["count"] = count
        resp = requests.get(url=url,params=params)
        if resp.status_code == 200:
            return resp.json()
        

    def get_search(self, keyword):
        url = self.DEFAULT_API_ENDPOINT + "/gfycats/search"
        params = {"search_text":keyword}
        resp = requests.get(url=url,params=params)
        if resp.status_code == 200:
            return resp.json()




    