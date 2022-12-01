from src.database.user_db import UserDB
from src.utils.errors_util import CommonError
from werkzeug.security import generate_password_hash


class UserService:
    def create_user(self, user_object):
        username_exist = UserDB().get_user_by_username(user_object.username)
        email_exist = UserDB().get_user_by_email(user_object.email)
        if username_exist or email_exist:
            raise CommonError(message="Ja existe um usuario com esse nome", status_code=400)

        user_object.password = generate_password_hash(user_object.password)
        user = UserDB().register_user(user_object)
        return user

    def get_user(self, user_id):
        user = UserDB().get_user_by_id(user_id)
        return user

    def edit_user(self, current_user, payload):
        for key, value in payload.items():
            current_user.key = value

        user = UserDB().update_user(current_user)
        return user
