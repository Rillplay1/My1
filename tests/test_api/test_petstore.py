import requests
import pytest
import random

#тут эта штука не нужна

# @pytest.fixture
# def obj_id():
#     payload = {
#         "id": random.randint(1, 60),
#         "category": {
#             "id": random.randint(1, 60),
#             "name": "python"
#         },
#         "name": "python",
#         "photoUrls": [
#             "string"
#         ],
#         "tags": [
#             {
#                 "id": random.randint(1, 60),
#                 "name": "sobaken"
#             }
#         ],
#         "status": "available"
#     }
#     response = requests.post("https://petstore.swagger.io/v2/pet", json=payload)
#     yield response.json()["id"]
#     requests.delete(f"https://petstore.swagger.io/v2/pet/{response.json()['id']}")
#

# def test_post_object():
#     payload = {
#   "id": 66,
#   "category": {
#     "id": 66,
#     "name": "python"
#   },
#   "name": "python",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 66,
#       "name": "sobaken"
#     }
#   ],
#   "status": "available"
# }
#     response = requests.post("https://petstore.swagger.io/v2/pet", json=payload)
#     assert response.status_code == 200
#
#     response = requests.delete("https://petstore.swagger.io/v2/pet/66")
#     assert response.status_code == 200
#
#
# def test_put_object():
#     payload = {
#   "id": 66,
#   "category": {
#     "id": 66,
#     "name": "C#"
#   },
#   "name": "c++",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 66,
#       "name": "kote"
#     }
#   ],
#   "status": "sold"
# }
#     response = requests.put("https://petstore.swagger.io/v2/pet", json=payload)
#     assert response.status_code == 200
#
#
# def test_get_object():
#     response = requests.get("https://petstore.swagger.io/v2/pet/2")
#     assert response.status_code == 200




