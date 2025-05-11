class Endpoint:
    response = None
    response_json = None



    def check_response_is_200(self):
        assert self.response.status_code == 200


    def check_response_id(self, obj_id):
        assert self.response_json["id"] == obj_id

    def check_response_is_404(self):
        assert self.response.status_code == 404

    def check_response_name(self, name):
        assert self.response_json["name"] == name