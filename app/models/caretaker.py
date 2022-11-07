from app import db
from flask import Blueprint, jsonify, abort, make_response, request

# Create the class that is inherited from the db.Model from SQLAlchemy
class Caretaker(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    dogs = db.relationship("Dog", back_populates="caretaker")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, request_body):
        return cls(
            name=request_body["name"]
        )

    def update(self, req_body):
        try: 
            self.name = req_body["name"]
        except KeyError as error:
            abort(make_response({'message': f"Missing attribute: {error}"}))


