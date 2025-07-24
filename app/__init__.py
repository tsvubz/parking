from flask import Flask

def create_app():
    app = Flask(__name__)


    from app.main.routes import main
    from app.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app