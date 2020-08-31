import random
from unittest import TestCase
import requests
import json

ins_num = random.randint(0, 200000)
test_url = 
end = 
test_end = test_url + end

class Test_For_Update_User_Endpoint(TestCase):

    def test_get_comments_no_entry_res(self):
        response = requests.patch(test_end)
        print(response.text)
        self.assertEqual(response.status_code, 400)

    def test_wrong_complaint_id_res(self):
        # Ensures wrong complaint id means 403 error
        data = {
        	'id': 1896
        }
        response = requests.patch(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(res['message'], "Complaint with id: {} does not exist".format(data['id']))

    def test_no_comment_res(self):
        # Ensures valid complaint id with no comments means 404 error
        data = {
            'id': 1
        }
        response = requests.patch(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res['message'], "No Comments")

    def test_comment_res(self):
        # Ensures valid complaint id with comments means 200 and success
        data = {
            'id': 3
        }
        response = requests.patch(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], "Retrieved comments Successfully")

if __name__ == '__main__':
    unittest.main()