import requests
import json


class GfycatCaller(object):
    DEFAULT_API_ENDPOINT = "https://api.gfycat.com/v1"
    TOKEN = None

    def __init__(
        self, client_id=None, client_secret=None, endpoint=DEFAULT_API_ENDPOINT
    ):
        self.endpoint = endpoint
        self.client_id = client_id
        self.client_secret = client_secret

    def set_token(self):
        url = self.DEFAULT_API_ENDPOINT + "/oauth/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }
        resp = requests.post(url=url, data=json.dumps(data))
        if resp.status_code == 200:
            self.TOKEN = resp.json["access_token"]
        return self

    def gfycat_content_parser(self, gyfcat_objs, selected_attrs):
        """
        return a list of dicts
        """
        return [{k: g.get(k) for k in selected_attrs} for g in gyfcat_objs]

    def get_trending(self, count=None, cursor=None):
        # no need for token
        url = self.DEFAULT_API_ENDPOINT + "/gfycats/trending"
        params = {}
        if count is not None:
            params["count"] = count
        if cursor is not None:
            params["cursor"] = cursor
        resp = requests.get(url=url, params=params)
        if resp.status_code != 200:
            return {"error": resp.json()}
        content = resp.json()
        cursor = None
        if "cursor" in content:
            cursor = content["cursor"]
        return (
            self.gfycat_content_parser(
                content["gfycats"], ["gifUrl", "numFrames", "views"]
            ),
            cursor,
        )

    def get_search(self, search_text, count=None, cursor=None):
        url = self.DEFAULT_API_ENDPOINT + "/gfycats/search"
        params = {"search_text": search_text}
        if count is not None:
            params["count"] = count
        if cursor is not None:
            params["cursor"] = cursor
        resp = requests.get(url=url, params=params)
        if resp.status_code != 200:
            return {"error": resp.json()}
        content = resp.json()
        cursor = None
        if "cursor" in content:
            cursor = content["cursor"]
        return (
            self.gfycat_content_parser(
                content["gfycats"], ["gifUrl", "numFrames", "views"]
            ),
            cursor,
        )
