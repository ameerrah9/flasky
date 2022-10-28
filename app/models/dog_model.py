# We need access to SQLAlchemy
from app import db

# Create the class that is inherited from the db.Model from SQLAlchemy
class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String, default="non-binary")