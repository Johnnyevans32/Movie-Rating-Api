import random
from unittest import TestCase
import requests
import json
from flask import jsonify

ins_num = random.randint(0, 200000)
test_url = 'https://movie-rating-api.herokuapp.com/'
end = '/v1/user/create'
test_end = test_url + end
class Test_For_Create_User_Endpoint(TestCase):

    def test_user_with_no_entry_response(self):

        response = requests.post(test_end)
        self.assertEqual(response.status_code, 400)

    def test_user_response(self):
        # Ensures valid input means 201
        data = {
            'name': 'example',
            'email': 'example@example.com' + ins_num,
            'password': 'example'
        }
        response = requests.post(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(res['message'], "Create Success")

    def test_user_invalid_response(self):
        # Ensures valid input means 400 error
        data = {
            'name': 'example',
            'email': 1,
            'password': 'example'
        }
        response = requests.post(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

