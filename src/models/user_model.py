from src.extensions.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    passowrd = db.Column(db.String(80), unique=False, nullable=False)
