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
    caretaker_id = db.Column(db.Integer, db.ForeignKey('caretaker.id'))
    caretaker = db.relationship("Caretaker", back_populates="dogs")

    def to_dict(self):
        dog_dict =  {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender
        }

        if self.caretaker_id:
            dog_dict["caretaker_id"] = self.caretaker_id

        return dog_dict

    @classmethod
    def from_dict(cls, request_body):
        return cls(
            name=request_body["name"],
            breed=request_body["breed"],
            age=request_body["age"],
            gender=request_body["gender"]
        )

    def update(self, req_body):
        try: 
            self.name = req_body["name"]
            self.breed = req_body["breed"]
            self.age = req_body["age"]
            self.gender = req_body["gender"]
        except KeyError as error:
            abort(make_response({'message': f"Missing attribute: {error}"}))


