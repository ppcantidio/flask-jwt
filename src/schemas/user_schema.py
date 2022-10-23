from marshmallow import EXCLUDE, Schema, fields


class BaseUser(Schema):
    username = fields.Str()
    email = fields.Str()

    class Meta:
        unknow = EXCLUDE


class UserCreateSchema(BaseUser):
    password = fields.Str()


class UserOutSchema(BaseUser):
    id = fields.Int()
