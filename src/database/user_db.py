from src.extensions.database import db
from src.models.user_model import User as UserTable


class UserDB:
    def get_user_by_username(self, username: str):
        pass

    def get_user_by_id(self, user_id: str):
        pass

    def register_user(self, user: dict):
        user_object = UserTable(user)
        db.add(user_object)
        db.commit()
        db.refresh(user_object)
        return user_object
