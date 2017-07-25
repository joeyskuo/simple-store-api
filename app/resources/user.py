from flask_restful import Resource, reqparse

from models.UserModel import UserModel


class Register(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required=str,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        required=str,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = Register.parser.parse_args()

        username = data['username']
        user = UserModel.find_by_username(username)

        if (user):
            return {"message": "Username '%s' already exists." % username}, 400
        else:
            UserModel(**data).save_to_db()
            return {"message": "User created successfully."}, 201


