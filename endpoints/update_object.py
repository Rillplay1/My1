import requests
from endpoints.base_endpoint import Endpoint


class UpdateObject(Endpoint):
    def update_by_id(self, obj_id, payload):
        self.response = requests.put(
            f"https://api.restful-api.dev/objects/{obj_id}", json=payload)
        self.response_json = self.response.json()