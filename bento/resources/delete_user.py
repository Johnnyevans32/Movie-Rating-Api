
from flask_restful import Resource

from flask_restful_swagger_2 import swagger

from bento.models import User, db, Movie


class DeleteUser(Resource):
    @swagger.doc({
        'tags': ['User'],
        'description': 'Delete a user',
        'parameters': [
            {
                'name': 'user_id',
                'description': 'User identifier',
                'in': 'path',
                'required': 'true',
                'type': 'integer'
            }
        ],
        'responses': {
            '204': {
                'description': 'Delete Success',
                'examples': {
                    'application/json': {
                        'id': 1
                    }
                }
            },
            '404': {
                'description': 'Delete Failure'
            }
        }
    })

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            resp = {
                "status": "Failure",
                "message": "user not found thus Delete Failure",
                "result": ""
            }

            return resp, 404

        else:
            try:
                movies = Movie.query.filter_by(user_id=user_id).all()
                for movie in movies:
                    db.session.delete(movie)                        
                db.session.delete(user)
                db.session.commit()

                resp = {
                    "status": "Success",
                    "message": "Delete Success",
                    "result": ""
                }

                return resp, 204
            except Exception as e:
                print(e)
                resp = {
                    "status": "Failure",
                    "message": "Unexpected Error Occurred"
                }

                return resp, 400