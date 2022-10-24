from flask import Blueprint, jsonify, abort, make_response

# Hardcode data
class Dog:
    def __init__(self, id, name, breed, age, gender):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender

# hardcoded database
DOGS = [
    Dog(1, 'John Cena', "pug", 34, "Male"),
    Dog(2, 'Snoop', "hair doberman", 14, "Female"),
    Dog(3, "Doug 'the Doctor', M.D.", "pompom", 10, "Male")
]

dogs_bp = Blueprint('dogs_bp', __name__, url_prefix='/dogs')

@dogs_bp.route('', methods=['GET'])
def get_all_dogs():
    dog_response = [vars(dog) for dog in DOGS]
    return jsonify(dog_response)

# GET ONE DOG? HOW?
@dogs_bp.route('/<id>', methods=['GET'])     
def get_one_dog(id):
    # return dog as a dict
    dog = validate_dog(id)
    return dog

# Validation function
def validate_dog(id):
    # handle invalid data types such as non-ints
    try:
        dog_id = int(id)
    except ValueError:
        return {
            "message": "Invalid dog id"
        }, 400

    # handle if id is not found
    for dog in DOGS:
        if dog.id == dog_id:
            return vars(dog)

    abort(make_response(jsonify(description="Resource not found"),404)) 
    
    


        



# def get_all_dogs():
    # dog_response = []
    # for dog in DOGS:
    #     print(vars(dog))
    #     dog_response.append(vars(dog))
        # dog_response.append({
        #     'id': dog.id,
        #     'name': dog.name,
        #     'age': dog.age,
        #     'breed': dog.breed,
        #     'gender': dog.gender
        # })

    # print(DOGS)
    # print(dog_response)
    # print(type(dog_response))
    # print(type(jsonify(dog_response)))
