import datetime

import jwt
from dynaconf import settings
from src.database.user_db import UserDB


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

        time_exp = datetime.datetime.now() + datetime.timedelta(hours=12)
        token = jwt.encode({"username": user.username, "exp": time_exp}, settings.get("SECRET_KEY"))
        return {"message": "Validated sucessfully", "token": token.decode("UTF=8"), "exp": time_exp}
