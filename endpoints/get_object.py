import requests
from endpoints.base_endpoint import Endpoint

class GetObject(Endpoint):
    def get_by_id(self, obj_id):
        self.response = requests.get(
            f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()


