from flask import Blueprint, jsonify, abort, make_response

class Cat:
  def __init__(self, id, name, color, personality):
    self.id = id
    self.name = name
    self.color = color
    self.personality = personality

cats = [
  Cat(1, "Luna", "grey", "naughty"), 
  Cat(2, "Orange Cat", "orange", "antagonistic"),
  Cat(3, "Big Ears", "grey and white", "sleepy")
]

bp = Blueprint("cats", __name__, url_prefix="/cats")

#==============================
#     GET ALL RESOURCES
#==============================
@bp.route("", methods=["GET"])
def get_all_cats():
  results_list = []
  for cat in cats: 
    results_list.append({
      "id": cat.id, 
      "name": cat.name, 
      "color": cat.color,
      "personality": cat.personality
    })
  return jsonify(results_list)

#==============================
#     GET ONE RESOURCE
#==============================
@bp.route("/<id>", methods=["GET"])
def get_one_cat(id):
  cat = validate_cat_id(id)

  return jsonify({
    "id": cat.id, 
    "name": cat.name, 
    "color": cat.color,
    "personality": cat.personality
  }), 200

#=======================================
# GET ONE RESOURCE -- CLUTTERED VERSION
#=======================================
# def get_one_cat(id):
#   try:
#     cat_id = int(id)
#   except:
#     return {"message": f"{id} is invalid"}, 400

#   for cat in cats:
#     if cat_id == cat.id:
#       return jsonify({
#         "id": cat.id, 
#         "name": cat.name, 
#         "color": cat.color,
#         "personality": cat.personality
#       }), 200
      
#   return {"message": f"{cat_id} not found"}, 404

#==============================
#     HELPER METHODS
#==============================
def validate_cat_id(id):
  try:
    cat_id = int(id)
  except:
    abort(make_response({"message":f"cat {id} is an invalid id"}, 400))

  for cat in cats:
    if cat_id == cat.id:
      return cat
      
  abort(make_response({"message":f"cat {id} not found"}, 404))