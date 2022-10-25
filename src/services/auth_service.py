import datetime

import jwt
from dynaconf import settings
from flask import jsonify
from src.database.user_db import UserDB
from werkzeug.security import check_password_hash


class AuthService:
    def auth_user(self, auth):
        """
        Responsabilty to check username and password and return a valid token to be used for 12 hours
        """
        username = auth.username
        password = auth.password

        user = UserDB().get_user_by_username(username)
        if not user:
            return {"message": "user not found"}

        if check_password_hash(user.password, password):
            time_exp = datetime.datetime.now() + datetime.timedelta(hours=12)
            token = jwt.encode({"username": user.username, "exp": time_exp}, settings.get("SECRET_KEY"))
            return {"message": "Validated sucessfully", "token": token.decode("UTF=8"), "exp": time_exp}

        return {"message": "Could not verify"}
