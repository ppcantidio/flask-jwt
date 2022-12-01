from src.database.abstract_db import AbstractDB
from src.database.models import User as UserTable
from src.extensions.database import db


class UserDB(AbstractDB):
    def __init__(self):
        self.table = UserTable

    def get_user_by_username(self, username: str):
        user = self.table.query.filter(self.table.username == username).first()
        return user

    def get_user_by_email(self, email):
        user = self.table.query.filter(self.table.email == email).first()
        return user
