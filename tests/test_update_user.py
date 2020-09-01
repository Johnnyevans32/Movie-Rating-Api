import random
from unittest import TestCase
import requests
import json

ins_num = random.randint(0, 200000)
test_url = 'https://movie-rating-api.herokuapp.com/'
end = '/v1/user/update/'
test_end = test_url + end

class Test_For_Update_User_Endpoint(TestCase):

    def test_user_no_entry_res(self):
        response = requests.patch(test_end + user_id)
        print(response.text)
        self.assertEqual(response.status_code, 400)

    def test_invalid_user_res(self):
        user_id = 'ss'
        data = {
            'name': '',
            'email':'',
            'password': ''
        }
        response = requests.patch(test_end + user_id,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['message'], "Bad Request")

    def test_valid_user_res(self):
        user_id = 1
        data = {
            'name': '',
            'email':'',
            'password': ''
        }
        response = requests.patch(test_end + user_id,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], "User Updated Successfully")

    def test_wrong_user_res(self):
        user_id = 9929922
        data = {
            'name': '',
            'email':'',
            'password': ''
        }
        response = requests.patch(test_end + user_id,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res['message'], "User Not Found")

if __name__ == '__main__':
    unittest.main()