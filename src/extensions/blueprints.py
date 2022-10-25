from src.routes.auth_route import auth_route
from src.routes.error_route import error_route
from src.routes.user_route import user_route


def init_app(app):
    app.register_blueprint(user_route, url_prefix="/user")
    app.register_blueprint(auth_route, url_prefix="/auth")
    app.register_blueprint(error_route)
