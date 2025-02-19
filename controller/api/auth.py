"""API Related stuff"""

import datetime
from os import environ
from dotenv import load_dotenv
from flask import jsonify, request
from werkzeug.security import check_password_hash
from jwt import encode as jwt_encode, decode as jwt_decode
from flask_restful import Api, Resource

from db import users_tbl

load_dotenv()

SECRET_KEY = environ.get("secret_key", "secret")
api = Api()


class Login(Resource):
    """Login"""
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if not all((username, password)):
            return jsonify(
                {
                    "status": "error",
                    "message": "Authorization failed. Required username/password fields to be filled.",
                }
            )

        user = users_tbl.select_one({"username": username})

        if check_password_hash(user.password, password):
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "Authorization failed. Invalid password",
                    }
                ),
                401,
            )

        token = jwt_encode(
            {
                "user": username,
                "exp": datetime.datetime.now(datetime.timezone.utc),
                'role': user.role
                + datetime.timedelta(days=2),
            },
            SECRET_KEY,
            algorithm="HS256",
        )
        return jsonify(
            {
                "status": "success",
                "message": "Authorization is completed",
                "token": token,
            }
        )

class Register(Resource):
    pass