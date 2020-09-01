import random
from unittest import TestCase
import requests
import json

ins_num = random.randint(0, 200000)
test_url = 'https://movie-rating-api.herokuapp.com/'
end = '/v1/movie/add'
test_end = test_url + end

class Test_For_Add_Movie_Endpoint(TestCase):

    def test_movie_with_no_entry_res(self):
        response = requests.post(test_end)
        self.assertEqual(response.status_code, 400)

    def test_movie_res(self):
        # Ensures valid input means 201
        data = {
            'user_id': 1,
            'title': 'game of thrones' + ins_num,
            'rating': 2
        }
        response = requests.post(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(res['message'], "Create Success")

    def test_movie_invalid_res(self):
        # Ensures invalid rating means 208 error
        data = {
            'user_id': 1,
            'title': 'game of thrones' + ins_num,
            'rating': 9
        }
        response = requests.post(test_end,
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 208)
        self.assertEqual(res['message'], "Rating must be between 1 to 5")

if __name__ == '__main__':
    unittest.main()
