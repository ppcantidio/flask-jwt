from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from src.database.models import User as UserTable
from src.schemas.user_schema import UserCreateSchema, UserOutSchema
from src.services.user_service import UserService
from src.utils.auth_util import token_required
from src.utils.responses_util import res_data_invalid, res_sucess

user_route = Blueprint("user_route", __name__)


class UserRoute:
    @user_route.route("/", methods=["POST"])
    def create_user():
        req_data = request.get_json() or None

        try:
            user_request = UserCreateSchema().load(req_data)
        except ValidationError as err:
            return res_data_invalid(err)

        user_object = UserTable(**user_request)
        UserService().create_user(user_object)

        return jsonify({"message": "user created with sucess"})

    @user_route.route("/<id>", methods=["GET"])
    @token_required
    def get_user(current_user, id):
        user = UserService().get_user(id)

        user = UserOutSchema().dump(user)

        return jsonify({"message": "user retrieved with sucess", "data": user})

    @user_route.route("/", methods=["PUT"])
    @token_required
    def edit_user(current_user):
        payload = request.json

        user = UserService().edit_user(payload)

        return jsonify({"user": user})
