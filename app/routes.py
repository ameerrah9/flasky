from flask import Blueprint, jsonify, abort, make_response

class Crystal:
    def __init__(self, id, name, color, powers):
        self.id = id
        self.name = name
        self.color = color
        self.powers = powers
        
# create a list of crystals
crystals = [
    Crystal(1, "Amethyst", "Purple", "Infinite knowledge and wisdom"),
    Crystal(2, "Tiger's Eye", "Gold", "Confidence, strength"),
    Crystal(3, "Rose Quarts", "Pink", "Love")
]
# responsible for validating and returning crytstal instance 
def validate_crystal(crystal_id):
    try:
        crystal_id = int(crystal_id)
    except:
        abort(make_response({"message": f"{crystal_id} is not a valid type ({type(crystal_id)}). Must be an integer)"}, 400))

    for crystal in crystals:
        if crystal.id == crystal_id:
            return crystal
    

    abort(make_response({"message": f"crystal {crystal_id} does not exist"}, 404))


crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

@crystal_bp.route("", methods=["GET"])
def handle_crystals():
    crystal_response = []
    for crystal in crystals:
        crystal_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
        })
        
    return jsonify(crystal_response)

# localhost:5000/crystals/1

# Determine representation and send back response
@crystal_bp.route("/<crystal_id>", methods=["GET"])
def  handle_crystal(crystal_id):

    crystal = validate_crystal(crystal_id)

    return {
        "id": crystal.id,
        "name": crystal.name,
        "color": crystal.color,
        "powers": crystal.powers
    }
    
