from flask import Blueprint, jsonify

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
    dog_response = []
    for dog in DOGS:
        dog_response.append({
            'id': dog.id,
            'name': dog.name,
            'age': dog.age,
            'breed': dog.breed,
            'gender': dog.gender
        })

    print(type(dog_response))
    print(type(jsonify(dog_response)))
    return jsonify(dog_response)
