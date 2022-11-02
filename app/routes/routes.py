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
  new_cat = Cat.from_dict(request_body)
  db.session.add(new_cat)
  db.session.commit()

  return make_response(f"Cat {new_cat.name} has been created", 201)

#==============================
#     GET ALL RESOURCES
#==============================
@bp.route("", methods=["GET"])
def get_all_cats():
  color_param = request.args.get("color")
  personality_param = request.args.get("personality")

  if color_param:
    cats = Cat.query.filter_by(color=color_param)
  elif personality_param:
    cats = Cat.query.filter_by(personality=personality_param)
  else:
    cats = Cat.query.all()

  result_list = [cat.to_dict() for cat in cats]
  
  return jsonify(results_list), 200

#==============================
#     GET ONE RESOURCE
#==============================
@bp.route("/<id>", methods=["GET"])
def get_one_cat(id):
  cat = validate_id(Cat,id)

  return jsonify(cat.to_dict()), 200

#==============================
#     UPDATE RESOURCE
#==============================
@bp.route("/<id>", methods=["PUT"])
def update_cat(id):
  cat = validate_id(Cat,id)
  request_body = request.get_json()

  cat.update(request_body)

  db.session.commit()

  return make_response(f"cat {id} successfully updated")

#==============================
#     DELETE RESOURCE
#==============================
@bp.route("/<id>", methods=["DELETE"])
def delete_cat(id):
  cat = validate_id(Cat,id)

  db.session.delete(cat)

  db.session.commit()

  return make_response(f"cat {id} successfully deleted")

#==============================
#     HELPER METHODS
#==============================
def validate_id(class_obj,id):
  try:
    id = int(id)
  except:
    abort(make_response({"message":f"{class_obj} {id} is an invalid id"}, 400))

  query_result = class_obj.query.get(id)
  if not query_result:
      abort(make_response({"message":f"{class_obj} {id} not found"}, 404))

  return query_result