
from flask_restful import Resource

from flask_restful_swagger_2 import swagger

from bento.models import User, Movie, movieSchema


class GetMovie(Resource):
    @swagger.doc({
        'tags': ['Movie'],
        'description': 'Retrieve movie by user id',
        'parameters': [
            {
                'name': 'user_id',
                'description': 'User identifier',
                'in': 'path',
                'type': 'integer'
            },
            {
                'name': 'title',
                'description': 'Movie identifier',
                'in': 'path',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'Retrieve Success',
                'examples': {
                    'application/json': {
                        'user_id': 1
                    },
                    'application/json': {
                        'title': 'game of thrones'
                    }
                }
            },
            '404': {
                'description': 'Not Found'
            },
            '403': {
                'description': 'Forbidden'
            }
        }
    })
    def get(self, user_id, title):
        tag = "_".join([str(user_id), title])
        movie = Movie.query.filter_by(movie_tag=tag).first()
        if movie is None:
            resp = {
                'status': 'Failure',
                'message': 'Movie Not Found',
                'result': ''
            }

            return resp, 404
        else:
            try:
                resp = {
                    'status': 'Success',
                    'message': 'Retrieve Success',
                    'result': movieSchema.dump(movies)
                }

                return resp, 200
            except Exception as e:
                print(e)
                resp = {
                    "status": "Failure",
                    "message": "Unexpected Error Occurred"
                }

                return resp, 400
        
