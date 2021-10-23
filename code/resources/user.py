import sqlite3
from flask_restful import Resource, reqparse
from models.user import Usermodel

class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str, required = True, help = "username required to register")
    parser.add_argument('password', type = str, required = True, help = "password required")

    def post(self):
        data = UserRegistration.parser.parse_args()
        if Usermodel.find_by_username(data['username']):
            return {"message": "user already exists"}, 400

        user=Usermodel(data['username'], data['password'])
        user.save_to_db()

        return{"message": "user created succesfully"}, 201
