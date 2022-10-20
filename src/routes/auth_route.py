from flask import Blueprint, request, jsonify


from src.services.auth_service import AuthService


auth_route = Blueprint("auth_route", __name__)


class AuthRoute:
    @auth_route.route("/", methods=["POST"])
    def auth_user():
        auth = request.authorization

        response = AuthService().auth_user(auth)

        return jsonify(response), 200
