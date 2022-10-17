from src.routes.users_routes import users_routes


def init_app(app):
    app.register_blueprint(users_routes)
