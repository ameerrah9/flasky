from crypt import methods
from app import db
from app.models.dog_model import Dog
from flask import Blueprint, jsonify, make_response, request

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

# ADD Post to Request
# ADD Get to Request
@dogs_bp.route("", methods=["GET", "POST"])
# Change name to handle dogs
def handle_dogs():
    if request.method == "GET":
        dogs = Dog.query.all()
        dogs_response = []
        for dog in dogs:
            dogs_response.append({
                "id": dog.id,
                "name": dog.name,
                "breed": dog.breed,
				"age": dog.age,
				"gender": dog.gender
            })
        return jsonify(dogs_response)
    elif request.method == "POST":
        request_body = request.get_json()

        # Feel free to add a guard clause
        if "name" not in request_body or "breed" not in request_body:
            return make_response("Invalid Request, Name & Breed Can't Be Empty", 400)
        # How we know about Dog
        new_dog = Dog(
        # You're looking for this key and assign it to name, breed, gender, age
        name=request_body["name"],
        breed=request_body["breed"],
        age=request_body["age"],
        gender=request_body["gender"]
    )

        # Add this new instance of dog to the database
        db.session.add(new_dog)
        db.session.commit()

        # Successful response
        return make_response(f"Dog {new_dog.name} has been successfully created!", 201)

# Path/Endpoint to get a single dog
# Include the id of the record to retrieve as a part of the endpoint
@dogs_bp.route("/<dog_id>", methods=["GET", "PUT", "DELETE"])
# GET /dog/id
def handle_dog(dog_id):
    # Query our db to grab the dog that has the id we want:
    dog = Dog.query.get(dog_id)

    if request.method == "GET":
        # Send back a single JSON object (dictionary):
        return {
            "id": dog.id,
            "name": dog.name,
            "breed": dog.breed,
            "age": dog.age,
            "gender": dog.gender
        }
    elif request.method == "PUT":
        request_body = request.get_json()

        # Updated dog attributes are set:
        dog.name = request_body["name"],
        dog.breed = request_body["breed"],
        dog.age = request_body["age"],
        dog.gender = request_body["gender"]

        # Update this dog in the database
        db.session.commit()

        # Sucessful response
        return make_response(f"Dog {dog.name} has been successfully updated!", 200)
    elif request.method == "DELETE":
        db.session.delete(dog)
        db.session.commit()

        return make_response(f"Dog {dog.name} successfully deleted", 202)