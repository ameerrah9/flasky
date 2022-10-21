from flask import Flask

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    from .routes.routes import bp
    app.register_blueprint(bp)

    return app