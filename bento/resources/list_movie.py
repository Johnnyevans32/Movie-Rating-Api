
from flask_restful import Resource
from flask_restful_swagger_2 import swagger

from bento.models import Movie, movie_schema_many


class ListMovie(Resource):
    @swagger.doc({
        'tags': ['Movie'],
        'description': 'Retrieve all Movie',
        'parameters': [],
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
    def get(self):
        movies = movie_schema_many.dump(Movie.query.all())
        resp = {
            "status": "Success",
            "message": "Retrieved users Successfully",
            "result": movies
        }
        return resp, 200
