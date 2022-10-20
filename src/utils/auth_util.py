from functools import wraps

import jwt
from dynaconf import settings
from flask import jsonify, request
from src.database.user_db import UserDB


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("API-TOKEN")
        if not token:
            return jsonify({"message": "token is missing", "data": []}), 401
        try:
            data = jwt.decode(token, settings["SECRET_KEY"])
            current_user = UserDB().get_user_by_username(username=data["username"])
        except:
            return jsonify({"message": "token is invalid or expired", "data": []}), 401
        return f(current_user, *args, **kwargs)

    return decorated
