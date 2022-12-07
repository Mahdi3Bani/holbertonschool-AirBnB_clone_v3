#!/usr/bin/python3
"""
all u need to manipulate the amenitiess
"""
from api.v1.app import app_views
from models import storage
from models.amenity import Amenity
from flask import jsonify, abort, request


@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
def get_amenities():
    """get amenities"""
    amenitiess = []
    for i in storage.all(Amenity).values():
        amenitiess.append(i.to_dict())

    return jsonify(amenitiess)


@app_views.route('/amenities/<amenity_id>/', strict_slashes=False, methods=['GET'])
def get_amenities(amenity_id):
    """get amenities"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', strict_slashes=False,
                 methods=['DELETE'])
def delete_amenities(amenity_id):
    """delete a amenities"""
    if not storage.get(Amenity, amenity_id):
        abort(404)
    storage.delete(storage.get(Amenity, amenity_id))
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/amenities', strict_slashes=False, methods=['POST'])
def post_amenities():
    """create a new amenities"""
    if not request.get_json():
        abort(400, "Not a JSON")

    if 'name' not in request.get_json():
        abort(400, "Missing name")

    req = request.get_json()
    obj = Amenity(**req)
    return (jsonify(obj.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=["PUT"])
def put_amenities(amenities_id):
    """Update a new amenities"""

    amenity = storage.get(Amenity, amenities_id)

    if not amenity:
        abort(404)

    if not request.get_json():
        abort(400, "Not a JSON")

    passs = ['id', 'created_at', 'updated_at']

    valeurs = request.get_json()

    for key, value in valeurs.items():
        if key not in passs:
            setattr(amenity, key, value)

    storage.save()
    return (jsonify(amenity.to_dict()), 200)
