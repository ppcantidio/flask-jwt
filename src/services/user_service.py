from src.database.user_db import UserDB


class UserService:
    def create_user(self, user_request):
        user = UserDB().register_user(user_request)
        return user

    def get_user(self, user_id):
        user = UserDB().get_user_by_id(user_id)
        return user

    def edit_user(self, payload):
        pass
