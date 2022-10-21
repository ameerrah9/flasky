from flask import Blueprint, jsonify

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

@bp.route("", methods=["GET"])
def handle_cats():
    results_list = []
    for cat in cats: 
        results_list.append(dict(
            id=cat.id, 
            name=cat.name, 
            color=cat.color,
            personality=cat.personality
        ))
    return jsonify(results_list)