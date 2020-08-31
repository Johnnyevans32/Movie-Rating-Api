import random
from unittest import TestCase
import requests
import json

test_url = 
end = '/v1/user/delete/'
test_end = test_url + end

class Test_For_Get_Complaint_by_ID_Endpoint(TestCase):

    def test_get_complaint_no_entry_res(self):
        
        response = requests.get(test_end)
        print(response.text)
        self.assertEqual(response.status_code, 400)

    def test_wrong_complaint_id_res(self):
        # Ensures wrong complaint id means 404 error
        data = {
        	'id': 1896
        }
        response = requests.get(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res['message'], "Not Found")


    def test_complaint_res(self):
        # Ensures valid complaint id means 200 and success
        data = {
            'id': 3
        }
        response = requests.get(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], "Retrieve Success")

if __name__ == '__main__':
    unittest.main()