from flask_restful import reqparse, Resource
from flask_restful_swagger_2 import swagger
from bento.models import User, userSchema
from bento.models import User, db
from sqlalchemy.exc import IntegrityError
import hashlib
from passlib.hash import sha256_crypt

class CreateUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('email', required=True)
        self.parser.add_argument('password', required=True)

    @swagger.doc({
        'tags': ['User'],
        'description': 'Create User',
        'parameters': [
            {
                'name': 'body',
                'description': 'Details of the User',
                'in': 'body',
                'schema': {
                    'type': 'string',
                    'required': 'true',
                    'example': {
                        'name': 'example',
                        'email': 'example@example.com',
                        'password': 'example'
                    }
                }
            }
        ],
        'responses': {
            '201': {
                'description': 'Create Success',
                'examples': {
                    'application/json': {
                        'name': 'example',
                        'email': 'example@example.com',
                        'password': 'example'
                    }
                }
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
        password = sha256_crypt.hash(str(args.get('password')))
        user = User(
            email=args.get('email'),
            name=args.get('name'),
            password=password
        )
        try:
            db.session.add(user)
            db.session.commit()
            resp = {
                "status": "Success",
                "message": "Create Success",
                "result": userSchema.dump(user)
            }
            return resp, 201

        except IntegrityError:
            resp = {
                "status": "Failure",
                "message": "User with that email already exist!"
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
