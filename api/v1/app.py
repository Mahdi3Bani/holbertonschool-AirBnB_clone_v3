#!/usr/bin/python3
"""
app
"""
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

from os import getenv

app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)


@app.errorhandler(404)
def handle_error(error):

    return jsonify({"error": "Not found", }), 404


@app.teardown_appcontext
def teardown_appcontext(self):

    storage.close()


if __name__ == "__main__":
    a = getenv("HBNB_API_HOST ", default='0.0.0.0')
    b = getenv('HBNB_API_PORT', default=5000)
    app.run(host=a, port=b, threaded=True)
