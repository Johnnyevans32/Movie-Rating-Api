from flask_restful import reqparse, Resource
from flask_restful_swagger_2 import swagger
from bento.models import Movie, User, movieSchema
from bento.models import db
from sqlalchemy.exc import IntegrityError


class UpdateMovie(Resource):

    @swagger.doc({
        'tags': ['Movie'],
        'description': 'Update the Rating of a Movie',
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
            },
            {
                'name': 'rating',
                'description': 'New Rating',
                'in': 'path',
                'type': 'integer'
            }

        ],
        'responses': {
            '201': {
                'description': 'Create Success',
                'examples': {
                    'application/json': {
                        'user_id': 1
                    },
                    'application/json': {
                        'title': 'game of thrones'
                    },
                    'application/json': {
                        'rating': 4
                    }

                }
            },
            '208': {
                'description': 'Rating must be between 1 to 5'
            },
            '400': {
                'description': 'Bad Request'
            },
            '403': {
                'description': 'Forbidden'
            },
            '404': {
                'description': 'Associated Movie Not Found'
            }
        }
    })
    def patch(self, user_id, title, rating):
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
            ratings = int(rating)
            if 1 <= ratings <= 5:
                try:
                    movie.rating = rating
                    db.session.add(movie)
                    db.session.commit()
                    resp = {
                        "status": "Success",
                        "message": "Movie Updated Successfully",
                        "result": movieSchema.dump(movie)
                    }
                    return resp, 201

                except IntegrityError:
                    resp = {
                        "status": "Failure",
                        "message": "Movie already added and rated!"
                    }
                    return resp, 403

                except Exception as e:
                    print(e)
                    resp = {
                        "status": "Failure",
                        "message": "Something went wrong",
                        "result": ''
                    }
                    return resp, 400
            else:
                resp = {
                    "status": "Failure",
                    "message": "Rating must be between 1 to 5"
                }
                return resp, 208
