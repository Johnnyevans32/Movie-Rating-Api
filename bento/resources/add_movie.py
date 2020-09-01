from flask_restful import reqparse, Resource
from flask_restful_swagger_2 import swagger
from bento.models import Movie, User, movieSchema
from bento.models import db
from sqlalchemy.exc import IntegrityError


class AddMovie(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user_id', required=True)
        self.parser.add_argument('title', required=True)
        self.parser.add_argument('rating', required=True)

    @swagger.doc({
        'tags': ['Movie'],
        'description': 'Add and Rate a Movie',
        'parameters': [
            {
                'name': 'body',
                'description': 'Details of the Movie',
                'in': 'body',
                'schema': {
                    'type': 'string',
                    'required': 'true',
                    'example': {
                        'user_id': 1,
                        'title': 'game of thrones',
                        'rating': 2
                    }
                }
            }
        ],
        'responses': {
            '201': {
                'description': 'Create Success',
                'examples': {
                    'application/json': {
                        'user_id': 1,
                        'title': 'game of thrones',
                        'rating': 2
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
                'description': 'Associated Complaint Not Found'
            }
        }
    })
    def post(self):

        args = self.parser.parse_args()
        user = User.query.filter_by(id=args.user_id).first()
        if user is None:
            resp = {
                'status': 'Failure',
                'message': 'User Not Found',
                'result': ''
            }

            return resp, 404
        else:
            rating = int(args.get('rating'))
            if 1 <= rating <= 5:
                movie = Movie(
                    user_id=args.get('user_id'),
                    title=args.get('title'),
                    rating=args.get('rating'),
                    movie_tag= "{}_{}".format(args.get('user_id'), args.get('title'))
                )
                try:
                    db.session.add(movie)
                    db.session.commit()
                    resp = {
                        "status": "Success",
                        "message": "Successful Movie rating",
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
