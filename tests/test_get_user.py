import random
from unittest import TestCase
import requests
import json

class Test_For_Get_Replies_by_Comment_ID_Endpoint(TestCase):

    def test_get_reply_no_entry_res(self):
        
        response = requests.get('http://complaint-microapi.herokuapp.com/v1/comment/<string:comment_id>/replies')
        print(response.text)
        self.assertEqual(response.status_code, 400)

    def test_wrong_comment_id_res(self):
        # Ensures wrong comment id means 400 error
        data = {
        	'id': 1896
        }
        response = requests.get('http://complaint-microapi.herokuapp.com/v1/comment/<string:comment_id>/replies',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['message'], "Bad Request")


    def test_reply_res(self):
        # Ensures valid comment id means 200 and success
        data = {
            'id': 3
        }
        response = requests.get('http://complaint-microapi.herokuapp.com/v1/comment/<string:comment_id>/replies',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], "Retrieve Success")

if __name__ == '__main__':
    unittest.main()