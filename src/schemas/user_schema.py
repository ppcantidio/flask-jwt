from marshmallow import Schema, fields


class BaseUser(Schema):
    name = fields.str()
    email = fields.str()


class UserCreateSchema(BaseUser):
    password = fields.str()


class UserOutSchema(BaseUser):
    id = fields.int()
