
from flask_restful import Resource
from flask_restful_swagger_2 import swagger

from bento.models import User, user_schema_many


class ListUser(Resource):
    @swagger.doc({
        'tags': ['User'],
        'description': 'Retrieve all users',
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
        users = user_schema_many.dump(User.query.all())
        resp = {
            "status": "Success",
            "message": "Retrieved users Successfully",
            "result": users
        }
        return resp, 200
