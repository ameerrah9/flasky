from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.crystal import Crystal

# class Crystal:
#     def __init__(self, id, name, color, powers):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.powers = powers
        
# create a list of crystals
# crystals = [
#     Crystal(1, "Amethyst", "Purple", "Infinite knowledge and wisdom"),
#     Crystal(2, "Tiger's Eye", "Gold", "Confidence, strength"),
#     Crystal(3, "Rose Quarts", "Pink", "Love")
# ]
# responsible for validating and returning crytstal instance 
# def validate_crystal(crystal_id):
#     try:
#         crystal_id = int(crystal_id)
#     except:
#         abort(make_response({"message": f"{crystal_id} is not a valid type ({type(crystal_id)}). Must be an integer)"}, 400))

#     for crystal in crystals:
#         if crystal.id == crystal_id:
#             return crystal
    

#     abort(make_response({"message": f"crystal {crystal_id} does not exist"}, 404))


crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

# @crystal_bp.route("", methods=["GET"])
# def handle_crystals():
#     crystal_response = []
#     for crystal in crystals:
#         crystal_response.append({
#             "id": crystal.id,
#             "name": crystal.name,
#             "color": crystal.color,
#             "powers": crystal.powers
#         })
        
#     return jsonify(crystal_response)

# localhost:5000/crystals/1

# Determine representation and send back response
# @crystal_bp.route("/<crystal_id>", methods=["GET"])
# def  handle_crystal(crystal_id):

#     crystal = validate_crystal(crystal_id)

#     return {
#         "id": crystal.id,
#         "name": crystal.name,
#         "color": crystal.color,
#         "powers": crystal.powers
#     }

# responsible for validating and returning crytstal instance 
def validate_crystal(crystal_id):
    try:
        crystal_id = int(crystal_id)
    except:
        abort(make_response({"message": f"{crystal_id} is not a valid type ({type(crystal_id)}). Must be an integer)"}, 400))

    crystal = Crystal.query.get(crystal_id)
    
    if not crystal:
        abort(make_response({"message": f"crystal {crystal_id} does not exist"}, 404))
        
    return crystal

@crystal_bp.route("", methods=['POST'])

# define a route for creating a crystal resource
def handle_crystals():
    request_body = request.get_json()
    
    new_crystal = Crystal(
        name = request_body["name"],
        color = request_body["color"],
        powers = request_body["powers"]
    )
    
    db.session.add(new_crystal)
    db.session.commit()
    
    return jsonify(f"Yayyyy Crystal {new_crystal.name} successfully created!"), 201

# define a route for getting all crystals
@crystal_bp.route("", methods=["GET"])
def read_all_crystals():
    
    # filter the crystal query results
    # to those whose color match the
    # query param
    color_query = request.args.get("color")
    # filter the crystal query results
    # to those whose powers match the
    # query param
    powers_query = request.args.get("powers")
    
    if color_query:
        crystals = Crystal.query.filter_by(color=color_query)
    elif powers_query:
        crystals = Crystal.query.filter_by(powers=powers_query)
    else:
        crystals = Crystal.query.all()
        
    crystals_response = []
    
    for crystal in crystals:
        crystals_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
        })
    
    return jsonify(crystals_response)

# define a route for getting a single crystal
# GET /crystals/<crystal_id>
@crystal_bp.route("/<crystal_id>", methods=["GET"])
def read_one_crystal(crystal_id):
    # Query our db to grab the crystal that has the id we want
    crystal = validate_crystal(crystal_id)
    
    # show a single crystal
    return {
        "id": crystal.id,
        "name": crystal.name,
        "color": crystal.color,
        "powers": crystal.powers
    }, 200

# define a route for updating a crystal
# PUT /crystals/<crystal_id>
@crystal_bp.route("/<crystal_id>", methods=["PUT"])
def update_crystal(crystal_id):
    # Query our db to grab the crystal that has the id we want
    crystal = validate_crystal(crystal_id)
    
    request_body = request.get_json()
    
    crystal.name = request_body["name"]
    crystal.color = request_body["color"]
    crystal.powers = request_body["powers"]

    db.session.commit()
    
    # send back the updated crystal
    return {
        "id": crystal.id,
        "name": crystal.name,
        "color": crystal.color,
        "powers": crystal.powers
    }, 200
    
# define a route for deleting a crystal
# DELETE /crystals/<crystal_id>
@crystal_bp.route("/<crystal_id>", methods=["DELETE"])
def delete_crystal(crystal_id):
    crystal = validate_crystal(crystal_id)
    
    db.session.delete(crystal)
    db.session.commit()
    
    return make_response(f"Crystal #{crystal.id} successfully deleted")