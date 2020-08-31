
from flask_restful import Resource

from flask_restful_swagger_2 import swagger

from bento.models import User, userSchema


class GetUser(Resource):
    @swagger.doc({
        'tags': ['User'],
        'description': 'Retrieve a single user by id',
        'parameters': [
            {
                'name': 'user_id',
                'description': 'User identifier',
                'in': 'path',
                'type': 'integer'
            }
        ],
        'responses': {
            '200': {
                'description': 'Retrieve Success',
                'examples': {
                    'application/json': {
                        'id': 1
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
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            resp = {
                'status': 'Failure',
                'message': 'User Not Found',
                'result': ''
            }

            return resp, 404
        else:
            try:
                resp = {
                    'status': 'Success',
                    'message': 'Retrieve Success',
                    'result': userSchema.dump(user)
                }

                return resp, 200
            except Exception as e:
                print(e)
                resp = {
                    "status": "Failure",
                    "message": "Unexpected Error Occurred"
                }

                return resp, 400
        
