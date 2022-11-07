from crypt import methods
from app import db
from app.models.dog_model import Dog
from app.routes.routes_helper import error_message, get_record_by_id
from flask import Blueprint, jsonify, make_response, request

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

# ADD Post to Request
# ADD Get to Request
# http://localhost:5000/dogs?breed=dachshund&age=1
@dogs_bp.route("", methods=["GET"])
# Change name to handle dogs
def handle_dogs():
    dog_query = Dog.query

    breed_query = request.args.get("breed")
    if breed_query:
        # exact string matching - case sensitive
        # dog_query = dog_query.filter_by(breed=breed_query)
        # partial filters - case sensitive
        # dog_query = dog_query.filter(Dog.breed.contains(breed_query))
        # partial filter - case insensitive
        dog_query = dog_query.filter(Dog.breed.ilike(f"%{breed_query}%"))

    age_query = request.args.get("age")
    if age_query:
        dog_query = dog_query.filter_by(age=age_query)

    dogs = Dog.query.all()

    # dogs_response = []
    # for dog in dogs:
    #     dogs_response.append({
    #         "id": dog.id,
    #         "name": dog.name,
    #         "breed": dog.breed,
    #         "age": dog.age,
    #         "gender": dog.gender
    #     })

    dogs_response = [dog.to_dict() for dog in dogs]

    # if not dogs_response:
    #     return make_response(jsonify(f"There are no {breed_query} dogs"))
    return jsonify(dogs_response), 200

@dogs_bp.route("", methods=["POST"])
# Change name to handle dogs
def create_dog():
    request_body = request.get_json()

    # Feel free to add a guard clause
    if "name" not in request_body or "breed" not in request_body:
        return make_response("Invalid Request, Name & Breed Can't Be Empty", 400)
    # How we know about Dog

    # new_dog = Dog(
    #     # You're looking for this key and assign it to name, breed, gender, age
    #     name=request_body["name"],
    #     breed=request_body["breed"],
    #     age=request_body["age"],
    #     gender=request_body["gender"]
    # )
    
    # refactored version
    new_dog = Dog.from_dict(request_body)

    # Add this new instance of dog to the database
    db.session.add(new_dog)
    db.session.commit()

    # Successful response
    return make_response(f"Dog {new_dog.name} has been successfully created!", 201)

# Path/Endpoint to get a single dog
# Include the id of the record to retrieve as a part of the endpoint
@dogs_bp.route("/<dog_id>", methods=["GET"])
# GET /dog/id
def handle_dog(dog_id):
    # Query our db to grab the dog that has the id we want:
    dog = get_record_by_id(Dog, dog_id)

    # Send back a single JSON object (dictionary):
    # return {
    #     "id": dog.id,
    #     "name": dog.name,
    #     "breed": dog.breed,
    #     "age": dog.age,
    #     "gender": dog.gender
    # }

    # refactored version
    return dog.to_dict(), 200

@dogs_bp.route("/<dog_id>", methods=["PUT"])
# PUT /dog/id
def edit_dog(dog_id):
    dog = Dog.query.get(dog_id)

    request_body = request.get_json()

    # Updated dog attributes are set:
    # dog.name = request_body["name"],
    # dog.breed = request_body["breed"],
    # dog.age = request_body["age"],
    # dog.gender = request_body["gender"]

    #refactored version
    dog.update(request_body)

    # Update this dog in the database
    db.session.commit()

    # Sucessful response
    return make_response(f"Dog {dog.name} has been successfully updated!", 200)

@dogs_bp.route("/<dog_id>", methods=["DELETE"])
# Delete /dog/id
def delete_dog(dog_id):
    dog = Dog.query.get(dog_id)

    db.session.delete(dog)
    db.session.commit()

    return make_response(f"Dog {dog.name} successfully deleted", 202)