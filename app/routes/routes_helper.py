from flask import jsonify, abort, make_response

def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))


def get_record_by_id(cls, id):
    # handled invalid data types
    try:
        id = int(id)
    except ValueError:
        error_message(f"Invalid id {id}", 400)

    # check if id exists in db
    model = cls.query.get(id)
    if model: 
        return model 

    error_message(f"No model of type {cls.__name__} with id {id} found", 404)