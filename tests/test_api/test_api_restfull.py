from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from conftest import *


def test_post_object():
  payload = {
     "name": "Apple MacBook Pro 16",
     "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
     }
  }
  new_obj_endpoint = CreateObject()
  new_obj_endpoint.new_object(payload=payload)
  new_obj_endpoint.check_response_is_200()


def test_get_object(obj_id):
  get_object_endpoint = GetObject()
  get_object_endpoint.get_by_id(obj_id)
  get_object_endpoint.check_response_is_200()
  get_object_endpoint.check_response_id(obj_id)


def test_put_object(obj_id):
  payload = {
     "name": "Apple MacBook Pro 16",
     "data": {
        "year": 2025,
        "price": 1949.89,
        "CPU model": "Intel Core i9",
        "Hard disk size": "5 TB"
     }
  }
  update_object_endpoint = UpdateObject()
  update_object_endpoint.update_by_id(obj_id, payload)
  update_object_endpoint.check_response_is_200()
  update_object_endpoint.check_response_name(payload["name"])


def test_delete_object(obj_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_id(obj_id)
    delete_object_endpoint.check_response_is_200()
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(obj_id)
    get_object_endpoint.check_response_is_404()
