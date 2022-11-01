from flask import Blueprint, jsonify, abort, make_response, request
from app.models.cat import Cat
from app import db

bp = Blueprint("cats", __name__, url_prefix="/cats")

#==============================
#       CREATE RESOURCE
#==============================
@bp.route("", methods=["POST"])
def create_cat():
  request_body = request.get_json()
  new_cat = Cat(
    name=request_body['name'], 
    personality=request_body['personality'], 
    color=request_body['color']
  )
  db.session.add(new_cat)
  db.session.commit()

  return make_response(f"Cat {new_cat.name} has been created", 201)

#==============================
#     GET ALL RESOURCES
#==============================
@bp.route("", methods=["GET"])
def get_all_cats():
  results_list = []
  all_cats = Cat.query.all()

  for cat in all_cats:
    results_list.append({
      "name": cat.name,
      "color": cat.color,
      "personality": cat.personality,
      "id": cat.id
    })
  
  return jsonify(results_list),200

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

#==============================
#     UPDATE RESOURCE
#==============================
@bp.route("/<id>", methods=["PUT"])
def update_cat(id):
  cat = validate_cat_id(id)
  request_body = request.get_json()

  cat.name = request_body["name"]
  cat.color = request_body["color"]
  cat.personality = request_body["personality"]

  db.session.commit()

  return make_response(f"cat {id} successfully updated")

#==============================
#     HELPER METHODS
#==============================
def validate_cat_id(id):
  try:
    cat_id = int(id)
  except:
    abort(make_response({"message":f"cat {id} is an invalid id"}, 400))

  cat = Cat.query.get(cat_id)
  if not cat:
      abort(make_response({"message":f"cat {id} not found"}, 404))

  return cat