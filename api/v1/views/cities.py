#!/usr/bin/python3
"""
all u need to manipulate the cities
"""
from api.v1.app import app_views
from models import storage
from models.state import State
from models.city import City
from flask import jsonify, abort, request


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False,
                 methods=['GET'])
def get_cities(state_id):
    """ger city"""
    if storage.get(State, state_id):
        abort(404)
    list_of_cities = []
    for i in storage.get(State, state_id).cities:
        list_of_cities.append(i.to_dict())

    return jsonify(list_of_cities)


@app_views.route('/cities/<city_id>',
                 strict_slashes=False,
                 methods=['GET'])
def get_city(city_id):
    """get city"""
    cityy = storage.get(State, city_id)
    if cityy is None:
        abort(404)

    return jsonify(cityy.to_dict())


@ app_views.route('/cities/<city_id>',
                  strict_slashes=False,
                  methods=['DELETE'])
def delete_city(city_id):
    """delete a city"""
    if not storage.get(City, city_id):
        abort(404)
    storage.delete(storage.get(State, city_id))
    storage.save()
    return (jsonify({}), 200)


@ app_views.route('/states/<state_id>/cities',
                  strict_slashes=False,
                  methods=['POST'])
def post_city(state_id):
    """create a new state"""
    if not storage.get(State, state_id):
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    req = request.get_json()
    obj = City(**req)
    obj.state_id = state_id
    obj.save()
    return (jsonify(obj.to_dict()), 201)


@ app_views.route('/cities/<city_id>', methods=["PUT"])
def put_state(city_id):
    """Update a new state"""

    city = storage.get(City, city_id)

    if not city:
        abort(404)

    if not request.get_json():
        abort(400, "Not a JSON")

    passs = ['id', 'created_at', 'updated_at']

    valeurs = request.get_json()

    for key, value in valeurs.items():
        if key not in passs:
            setattr(city, key, value)

    storage.save()
    return (jsonify(city.to_dict()), 200)
