import random
from unittest import TestCase
import requests
import json

ins_num = random.randint(0, 200000)
test_url = 'https://movie-rating-api.herokuapp.com/'
end = '/v1/movie/update/'
test_end = test_url + end

class Test_For_Update_Movie_Endpoint(TestCase):

    def test_movie_no_entry_res(self):
        response = requests.patch(test_end)
        print(response.text)
        self.assertEqual(response.status_code, 400)

    def test_invalid_user_res(self):
        user_id = 'ss'
        title = 'game of thrones'
        rating = 5
        response = requests.patch(test_end + user_id +'/'+ title +'/'+ rating)
        res = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['message'], "Bad Request")

    def test_valid_movie_res(self):
        user_id = 1
        title = 'game of thrones'
        rating = 5
        response = requests.patch(test_end + user_id +'/'+ title +'/'+ rating)
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], "Movie Updated Successfully")

    def test_wrong_movie_res(self):
        user_id = 9929922
        title = 'ga'
        rating = 5
        response = requests.patch(test_end + user_id +'/'+ title +'/'+ rating)
        res = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res['message'], "Movie Not Found")

if __name__ == '__main__':
    unittest.main()