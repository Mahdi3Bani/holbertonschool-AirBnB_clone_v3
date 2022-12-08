#!/usr/bin/python3
"""
all u need to manipulate the cities
"""
from api.v1.app import app_views
from models import storage
from models.place import Place
from models.city import City
from flask import jsonify, abort, request


@app_views.route('cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places(city_id):
    """ger places"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    list_of_places = []
    for i in city.places:
        list_of_places.append(i.to_dict())

    return jsonify(list_of_places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_palce(place_id):
    """get place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """delete a place"""
    if not storage.get(Place, place_id):
        abort(404)
    storage.delete(storage.get(Place, place_id)
                   )
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def post_place(city_id):
    """create a new state"""
    if not storage.get(City, city_id):
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    if 'user_id' not in request.get_json():
        abort(400, "Missing user_id")

    req = request.get_json()
    obj = Place(**req)
    obj.city_id = city_id
    obj.save()

    return (jsonify(obj.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """Update a new state"""

    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    if not request.get_json():
        abort(400, "Not a JSON")

    passs = ['id', 'created_at', 'updated_at']

    valeurs = request.get_json()

    for key, value in valeurs.items():
        if key not in passs:
            setattr(place, key, value)

    storage.save()
    return (jsonify(place.to_dict()), 200)
