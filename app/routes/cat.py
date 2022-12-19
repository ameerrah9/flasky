from app import db
from app.models.cat import Cat
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("cats", __name__, url_prefix="/cats")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@bp.route("/<id>", methods=["GET"])
def handle_cat(id):
    cat = validate_model(Cat, id)
    return jsonify(cat.to_dict()), 200

@bp.route("", methods=["POST"])
def create_cat():
    request_body = request.get_json()
    new_cat = Cat.from_dict(request_body)

    db.session.add(new_cat)
    db.session.commit()

    return jsonify(new_cat.to_dict()), 201

@bp.route("", methods=["GET"])
def read_all_cats():
    personality_query = request.args.get("personality")
    color_query = request.args.get("color")
    limit_query = request.args.get("limit")

    cat_query = Cat.query

    if personality_query:
        cat_query = cat_query.filter_by(personality=personality_query)

    if color_query:
        cat_query = cat_query.filter_by(color=color_query)

    if limit_query:
        cat_query = cat_query.limit(limit_query)

    cats = cat_query.order_by(Cat.id).all()

    cats_response = [cat.to_dict() for cat in cats]

    return jsonify(cats_response)

@bp.route("/<id>", methods=["PUT"])
def update_cat(id):
    cat = validate_model(Cat, id)
    request_body = request.get_json()

    cat.name = request_body["name"]
    cat.color = request_body["color"]
    cat.personality = request_body["personality"]
    cat.pet_count = request_body["pet_count"]

    db.session.commit()
    return jsonify(cat.to_dict())

@bp.route("/<id>/pet", methods=["PATCH"])
def pet_cat_with_id(id):
    cat = validate_model(Cat, id)
    cat.pet_count += 1

    db.session.commit()
    return jsonify(cat.to_dict())

@bp.route("/<id>", methods=["DELETE"])
def delete_cat(id):
    cat = validate_model(Cat, id)
    response_body = cat.to_dict()
    db.session.delete(cat)
    db.session.commit()
    return jsonify(response_body)
    