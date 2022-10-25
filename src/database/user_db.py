from src.database.models import User as UserTable
from src.extensions.database import db


class UserDB:
    def get_user_by_username(self, username: str):
        user = UserTable.query.filter(UserTable.username == username).first()
        return user

    def get_user_by_id(self, user_id: str):
        user = db.session.query(UserTable).get(user_id)
        return user

    def get_user_by_email(self, email):
        user = UserTable.query.filter(UserTable.email == email).first()
        return user

    def register_user(self, user_object: object):
        db.session.add(user_object)
        db.session.commit()
        db.session.refresh(user_object)
