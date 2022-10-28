from flask import Flask
# Translator from Flask to SQL
from flask_sqlalchemy import SQLAlchemy

# Migrater tool, helps us keep track of chances to our table
# "Versioning Control"
from flask_migrate import Migrate

    # Creating our Databse through our Instance of SQLAlchemy
    # Create Instances of Imports
    # GIve us access to the database operations

    # Database Representation
db = SQLAlchemy()

    # Migrations Respresentation
migrate = Migrate()

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # Where I am listening for my database
    # Ignore a warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # Connects Flask to the Database
    # Tells FLask where to find our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'


    # Connects db to migrate to our FLask app
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.dogs import dogs_bp
    app.register_blueprint(dogs_bp)

    return app