import requests
from endpoints.base_endpoint import Endpoint


class CreateObject(Endpoint):
    def new_object(self, payload):
        self.response = requests.post(
            "https://api.restful-api.dev/objects", json=payload)
        self.response_json = self.response.json()





