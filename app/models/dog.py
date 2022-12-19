# We need access to SQLAlchemy
from app import db
from flask import abort, make_response


# Create the class that is inherited from the db.Model from SQLAlchemy
class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String, default="non-binary")
    cuteness = db.Column(db.Integer)
    petCount = db.Column(db.Integer)
    caretaker_id = db.Column(db.Integer, db.ForeignKey('caretaker.id'))
    caretaker = db.relationship("Caretaker", back_populates="dogs")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender,
            "cuteness": self.cuteness,
            "petCount": self.petCount
        }

    @classmethod
    def from_dict(cls, request_body):
        return cls(
            name=request_body["name"],
            breed=request_body["breed"],
            age=request_body["age"],
            gender=request_body["gender"],
            cuteness=request_body["cuteness"],
            petCount=request_body["petCount"]
        )

    def update(self, req_body):
        try: 
            self.name = req_body["name"]
            self.breed = req_body["breed"]
            self.age = req_body["age"]
            self.gender = req_body["gender"]
            self.cuteness = req_body["cuteness"]
            self.petCount = req_body["petCount"]
        except KeyError as error:
            abort(make_response({'message': f"Missing attribute: {error}"}))


