from app import db
from app.models.caretaker import Caretaker
from app.models.cat import Cat
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("caretakers", __name__, url_prefix="/caretakers")


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} not found"}, 404))

    return model


@bp.route("", methods=["POST"])
def create_caretaker():
    request_body = request.get_json()
    new_caretaker = Caretaker.from_dict(request_body)

    db.session.add(new_caretaker)
    db.session.commit()

    return make_response(f"Caretaker {new_caretaker.name} successfully created", 201)


@bp.route("", methods=["GET"])
def read_all_caretakers():
    caretakers = Caretaker.query.all()

    caretakers_response = [caretaker.to_dict() for caretaker in caretakers]

    return jsonify(caretakers_response)


@bp.route("/<caretaker_id>/cats", methods=["POST"])
def create_cat(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    request_body = request.get_json()
    new_cat = Cat.from_dict(request_body)
    new_cat.caretaker = caretaker

    db.session.add(new_cat)
    db.session.commit()

    return make_response(f"Cat {new_cat.name} cared for by {caretaker.name}", 201)


@bp.route("/<caretaker_id>/cats", methods=["GET"])
def read_cats(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)

    cats_response = []
    for cat in caretaker.cats:
        cats_response.append(cat.to_dict())

    return(jsonify(cats_response))
