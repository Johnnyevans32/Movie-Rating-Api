from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger
from datetime import datetime
from bento.models import User, userSchema, db
import hashlib


class UpdateUser(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('email', required=True)
        self.parser.add_argument('password', required=True)

    @swagger.doc({
        'tags': ['User'],
        'description': 'Update a User',
        'parameters': [
            {
                'name': 'user_id',
                'description': 'The id of User to update',
                'in': 'path',
                'type': 'integer',
                'required': 'true'
            },
            {
                'name': 'body',
                'description': 'Description of User',
                'in': 'body',
                'schema': {
                    'type': 'string',
                    'required': 'false',
                    'example': {
                        'name': '',
                        'email':'',
                        'password': ''
                    }
                }
            }
        ],
        'responses': {
            '200': {
                'description': 'Update Success',
                'examples': {
                    'application/json': {
                        'title': 'Foo Bar',
                        'message': '-- because we have no imagination',
                        'status': 'closed',
                        'user_id': '2433'
                    }
                }
            },
            '400': {
                'description': 'Bad Request'
            },
            '404': {
                'description': 'Not Found'
            }
        }
    })
    def patch(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            resp = {
                'status': 'Update Failure',
                'message': 'User Not Found',
                'result': ''
            }
            return resp, 404
        else:
            try:
                args = self.parser.parse_args()
                for arg in args:
                    if args[arg] and arg in User.__dict__:
                        setattr(User, arg, args[arg])
                user.updated_at = datetime.utcnow()
                password = hashlib.sha1(str(args.get('password')).encode('utf-8')).hexdigest().upper()
                user.password = password
                db.session.add(user)
                db.session.commit()
                resp = {
                    'status': 'Update Success',
                    'message': 'User Updated Successfully',
                    'result': userSchema.dump(user)
                }
                return resp, 200
                
            except Exception as e:
                resp = {
                    'status': 'Update Failure',
                    'message': 'Bad Request',
                    'result': ''
                }
                return resp, 400
