from flask import Blueprint, jsonify, request
from services.user_service import UserService
from src.schemas.user_schema import UserCreateSchema, UserOutSchema
from src.utils.auth_util import token_required
from utils.responses_util import res_data_invalid

user_route = Blueprint("user_route", __name__)


class UserRoute:
    @user_route.route("/", methods=["POST"])
    def create_user():
        req_data = request.get_json() or None

        user_request, errors = UserCreateSchema().load(req_data)
        if errors:
            return res_data_invalid(errors)

        retorno = UserService().create_user(user_request)

        retorno = UserOutSchema().load(retorno)

    @user_route.route("/", methods=["PUT"])
    @token_required
    def edit_user(current_user):
        payload = request.json

        user = UserService().edit_user(payload)

        return jsonify({"user": user})
