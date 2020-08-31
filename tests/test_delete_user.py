import random
from unittest import TestCase
import requests
import json
import random

test_url = 
end = '/v1/user/delete/'
test_end = test_url + end

class Test_For_Delete_User_Endpoint(TestCase):

    def test_delete_user_with_no_entry_res(self):
        response = requests.delete(test_end)
        self.assertEqual(response.status_code, 400)

    def test_delete_user_res(self):
        # Ensures valid input means 204
        user_id = 1
        response = requests.delete(test_end + user_id)
        res = response.json()
        self.assertEqual(response.status_code, 204)
        self.assertEqual(res['message'], "Delete Success")

    def test_delete_user_invalid_res(self):
        # Ensures invalid input means 404 error
        user_id = 'sss'
        response = requests.delete(test_end + user_id)
        res = response.json()
        self.assertEqual(response.status_code, 500)
        self.assertEqual(res['message'], "Internal Server Error")

if __name__ == '__main__':
    unittest.main()
