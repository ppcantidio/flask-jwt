from flask import Blueprint


users_routes = Blueprint("users_routes", __name__)


class UsersRoutes:
    @users_routes.route("/", methods=["POST"])
    def create_user():
        pass
