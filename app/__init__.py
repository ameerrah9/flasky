from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# dotenv allows us to read env variables
from dotenv import load_dotenv
import os
load_dotenv() 

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    # Connects Flask to the Database
    # Tells FLask where to find our database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Connects db to migrate to our FLask app
    db.init_app(app)
    migrate.init_app(app, db)

    # Add import for Dog, Caretaker
    from app.models.dog_model import Dog
    from app.models.caretaker import Caretaker


    from .routes.dogs import dogs_bp
    app.register_blueprint(dogs_bp)

    from .routes.caretaker_routes import caretaker_bp
    app.register_blueprint(caretaker_bp)

    return app