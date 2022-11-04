from app import db

# Create the class that is inherited from the db.Model from SQLAlchemy
class Caretaker(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    dogs = db.relationship("Dog", back_populates="caretaker")