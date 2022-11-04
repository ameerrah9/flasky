from app import db
from app.models.caretaker import Caretaker
from app.models.dog_model import Dog
from flask import Blueprint, jsonify, abort, make_response, request

caretaker_bp = Blueprint("caretaker_bp", __name__, url_prefix="/caretakers")

@caretaker_bp.route("", methods=["POST"])
def create_caretaker():
    request_body = request.get_json()
    new_caretaker = Caretaker(name=request_body["name"])

    db.session.add(new_caretaker)
    db.session.commit()

    return make_response(jsonify(f"Caretaker {new_caretaker.name} successfully created"), 201)

@caretaker_bp.route("", methods=["GET"])
def read_all_caretaker():
    caretakers = Caretaker.query.all()

    caretaker_response = []
    for caretaker in caretakers:
        caretaker_response.append(
            {
                "id": caretaker.id,
                "name": caretaker.name
            }
        )
    return jsonify(caretaker_response)

# NESTED ROUTES
@caretaker_bp.route("/<id>/dogs", methods=["POST"])
def create_dog(id):
    caretaker = Caretaker.query.get(id)

    request_body = request.get_json()
    new_dog = Dog(
        name=request_body["name"],
        age=request_body["age"],
        gender=request_body["gender"],
        breed=request_body["breed"],
        caretaker=caretaker)

    db.session.add(new_dog)
    db.session.commit()

    return make_response(jsonify(f"Dog {new_dog.name} cared by {caretaker.name} successfully created"), 201)

@caretaker_bp.route("/<id>/dogs", methods=["GET"])
def read_dogs_of_caretaker(id):
    caretaker = Caretaker.query.get(id)

    print(caretaker.dogs)

    # dog_response = []
    # for dog in caretaker.dogs:
    #     dog_response.append(dog.to_dict()) #or dictionary literal

    dog_response = [dog.to_dict() for dog in caretaker.dogs]

    return(jsonify(dog_response))