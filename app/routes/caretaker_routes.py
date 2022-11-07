from flask import Blueprint, jsonify, abort, make_response, request
from app.models.cat import Cat
from app.models.caretaker import Caretaker
from app import db

ct_bp = Blueprint("caretakers", __name__, url_prefix="/caretakers")

@ct_bp.route("", methods=["POST"])
def create_caretaker():
  request_body = request.get_json()
  new_ct = Caretaker.from_dict(request_body)
  db.session.add(new_ct)
  db.session.commit()

  return make_response(f"Caretaker {new_ct.name} has been created", 201)

@ct_bp.route("/<ct_id>/cats", methods=["POST"])
def create_cat(ct_id):
  caretaker_query = Caretaker.query.get(ct_id)

  request_body = request.get_json()
  new_cat = Cat(
    name=request_body['name'], 
    personality=request_body['personality'], 
    color=request_body['color'],
    caretaker=caretaker_query
  )
  db.session.add(new_cat)
  db.session.commit()

  return make_response(f"Cat {new_cat.name} has been created", 201)