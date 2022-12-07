#!/usr/bin/python3
"""

"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats',  methods=['GET'], strict_slashes=False)
def number_of_object():
    '''
    retrieves the number of each objects by type
    '''
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    dic = {}
    for i in classes:
        dic[i] = storage.count(classes[i])

    return jsonify(dict)
