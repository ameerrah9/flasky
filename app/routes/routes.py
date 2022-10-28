from app import db
from app.models.cat import Cat
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("cats", __name__, url_prefix="/cats")

def validate_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except:
        abort(make_response({"message":f"cat {cat_id} invalid"}, 400))

    for cat in cats: 
        if cat.id == cat_id:
            return cat

    abort(make_response({"message":f"cat {cat_id} not found"}, 404))

# @bp.route("/<id>", methods=["GET"])
# def handle_cat(id):
#     cat = validate_cat(id)
#     return jsonify(cat.to_cat_dict())

@bp.route("", methods=["POST"])
def create_cat():
    request_body = request.get_json()
    new_cat = Cat(name=request_body["name"],
        color=request_body["color"],
        personality=request_body["personality"])

    db.session.add(new_cat)
    db.session.commit()

    return make_response(f"Cat {new_cat.name} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_cats():
    cats = Cat.query.all()
    cats_response = [cat.to_dict() for cat in cats]
    return jsonify(cats_response)


