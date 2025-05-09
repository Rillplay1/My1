# import requests
# import pytest
#
# @pytest.fixture
# def obj_id():
#     payload = {
#         "name": "Apple MacBook Pro 16",
#         "data": {
#             "year": 2019,
#             "price": 1849.99,
#             "CPU model": "Intel Core i9",
#             "Hard disk size": "1 TB"
#         }
#     }
#
#     response = requests.post("https://api.restful-api.dev/objects", json=payload)
#     yield response.json()["id"]
#     requests.delete(f"https://api.restful-api.dev/objects/{response.json()['id']}")
#
#
# def test_post_object():
#   payload = {
#      "name": "Apple MacBook Pro 16",
#      "data": {
#         "year": 2019,
#         "price": 1849.99,
#         "CPU model": "Intel Core i9",
#         "Hard disk size": "1 TB"
#      }
#   }
#   response = requests.post("https://api.restful-api.dev/objects", json=payload)
#   assert response.status_code == 200
#   assert "id" in response.json().keys()
#
#
# def test_get_object(obj_id):
#   print(obj_id)
#   response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}")
#   assert response.status_code == 200
#   data = response.json()
#   assert data["id"] == obj_id
#
#
# def test_put_object(obj_id):
#   payload = {
#      "name": "Apple MacBook Pro 16",
#      "data": {
#         "year": 2025,
#         "price": 1949.89,
#         "CPU model": "Intel Core i9",
#         "Hard disk size": "5 TB"
#      }
#   }
#   response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}",json=payload)
#   assert response.status_code == 200
#
#
# def test_delete_object(obj_id):
#     response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
#     assert response.status_code == 200
#     response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}")
#     assert response.status_code == 404
