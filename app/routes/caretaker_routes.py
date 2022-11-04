from app import db
from app.models.caretaker import Caretaker
from flask import Blueprint, jsonify, abort, make_response, request

caretaker_bp = Blueprint("caretaker_bp", __name__, url_prefix="/caretakers")

@caretaker_bp.route("", methods=["POST"])
def create_caretaker():
    request_body = request.get_json()
    new_caretaker = Caretaker(name=request_body["name"],)

    db.session.add(new_caretaker)
    db.session.commit()

    return make_response(jsonify(f"Caretaker {new_caretaker.name} successfully created"), 201)

@caretaker_bp.route("", methods=["GET"])
def read_all_caretaker():
    caretakers = Caretaker.query.all()

    caretaker_response = []
    for caretaker in caretakers:
        caretaker_response.append(
            {
                "name": caretaker.name
            }
        )
    return jsonify(caretaker_response)