from app import db
from app.models.cat import Cat
from flask import Blueprint, jsonify, abort, make_response


bp = Blueprint("cats", __name__, url_prefix="/cats")

@bp.route("", methods=["GET"])
def handle_cats():
    results_list = []
    for cat in cats: 
        results_list.append(cat.to_cat_dict())
    return jsonify(results_list)

def validate_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except:
        abort(make_response({"message":f"cat {cat_id} invalid"}, 400))

    for cat in cats: 
        if cat.id == cat_id:
            return cat

    abort(make_response({"message":f"cat {cat_id} not found"}, 404))

@bp.route("/<id>", methods=["GET"])
def handle_cat(id):
    cat = validate_cat(id)
    return jsonify(cat.to_cat_dict())

