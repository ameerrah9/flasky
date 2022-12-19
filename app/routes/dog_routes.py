from crypt import methods
from app import db
from app.models.dog import Dog
from app.routes.routes_helper import *
from flask import Blueprint, jsonify, make_response, request

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

@dogs_bp.route("", methods=["GET"])
def handle_dogs():
    dog_query = Dog.query

    breed_query = request.args.get("breed")
    if breed_query:
        dog_query = dog_query.filter(Dog.breed.ilike(f"%{breed_query}%"))

    age_query = request.args.get("age")
    if age_query:
        dog_query = dog_query.filter_by(age=age_query)

    dogs = Dog.query.all()

    dogs_response = [dog.to_dict() for dog in dogs]

    return jsonify(dogs_response), 200

@dogs_bp.route("", methods=["POST"])
def create_dog():
    request_body = request.get_json()

    if "name" not in request_body or "breed" not in request_body:
        return make_response("Invalid Request, Name & Breed Can't Be Empty", 400)
    
    new_dog = Dog.from_dict(request_body)

    db.session.add(new_dog)
    db.session.commit()

    return make_response(f"Dog {new_dog.name} has been successfully created!", 201)


@dogs_bp.route("/<dog_id>", methods=["GET"])

def handle_dog(dog_id):
    dog = get_record_by_id(Dog, dog_id)
    return dog.to_dict()

@dogs_bp.route("/<dog_id>", methods=["PUT"])
def edit_dog(dog_id):
    dog = get_record_by_id(Dog, dog_id)
    request_body = request.get_json()
    dog.update(request_body)
    db.session.commit()

    return make_response(f"Dog {dog.name} has been successfully updated!", 200)

@dogs_bp.route("/<dog_id>", methods=["DELETE"])
def delete_dog(dog_id):
    dog = get_record_by_id(Dog, dog_id)

    db.session.delete(dog)
    db.session.commit()

    return make_response(f"Dog {dog.name} successfully deleted", 202)

@dogs_bp.route("/<dog_id>", methods=["PATCH"])
def update_dog_pet_count(dog_id):
    dog = get_record_by_id(Dog, dog_id)

    dog.petCount += 1
    db.session.commit()

    return make_response(f"Dog {dog.name} successfully petted", 202)