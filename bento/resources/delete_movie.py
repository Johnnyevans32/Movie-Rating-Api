
from flask_restful import Resource

from flask_restful_swagger_2 import swagger

from bento.models import User,db, Movie, movie_schema_many


class DeleteMovie(Resource):
    @swagger.doc({
        'tags': ['Movie'],
        'description': 'Delete a movie from a user\'s list',
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
    def delete(self, user_id, title):
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
                name = movie.title
                db.session.delete(movie)
                db.session.commit() 

                resp = {
                    'status': 'Success',
                    'message': 'Delete Done'
                }

                return resp, 200
            except Exception as e:
                print(e)
                resp = {
                    "status": "Failure",
                    "message": "Unexpected Error Occurred"
                }

                return resp, 400
        
