
from flask_restful import Resource
from flask_restful_swagger_2 import swagger

from bento.models import Movie, movie_schema_many
import requests
import json

API_KEY = 'eea4f399e1af6d56f7814b75b9743566'
class ListMovie(Resource):
    @swagger.doc({
        'tags': ['Movie'],
        'description': 'Retrieve all Movies available from the movie db',
        'parameters': [
            {
                'name': 'page_num',
                'description': 'page number identifier',
                'in': 'path',
                'required': 'true',
                'type': 'integer'
            }
        ],
        'responses': {
            '200': {
                'description': 'Retrieve Success',
                'examples': {
                    'application/json': {
                    }
                }
            },
            '400': {
                'description': 'Invalid Request'
            }
        }
    })
    def get(self, page_num):
        url = requests.get('https://api.themoviedb.org/3/discover/movie?api_key='
            +API_KEY+
            '&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page='
            +page_num)
        movies = url.json()
        result = movies['results']
        resp = {
            "status": "Success",
            "message": "Retrieved Movies Successfully",
            "result": result
        }
        return resp, 200
