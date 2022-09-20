#!/usr/bin/python3
"""
RESTfull API states, manages states
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", strict_slashes=False, methods=['GET'])
def states():
    """
    Display states
    """
    states = storage.all("State")
    list_states = []
    for state in states.values():
        list_states.append(state.to_dict())
    return(jsonify(list_states))


@app_views.route('/states/<state_id>', strict_slashes=False,
                 methods=['GET'])
def states_id(state_id):
    """
    Display a state by its ID
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return(jsonify(state.to_dict()))


@app_views.route('/states', strict_slashes=False, methods=['POST'])
def create_state():
    """
    Creates a state
    """
    if not reques.get_json():
        error = {"error": "Not a JSON"}
        return(jsonify(error), 400)
    if "name" not in request.get_json():
        no_name = {"error": "Missing name"}
        return(jsonify(no_name), 400)
    obj_dict = request.get_json()
    state = State(**obj_dict)
    state.save()
    retur(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def update_state(state_id):
    """
    Updates a State
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        error = {"error": "Not a JSON"}
        return(jsonify(error), 400)
    obj_dict = request.get_json()
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key in obj_dict.keys():
        if key not in ignore_key:
            setattr(state, key, obj_dict[key])
    state.save()
    return(jsonify(state.to_dict()), 200)
