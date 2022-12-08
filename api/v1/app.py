#!/usr/bin/python3
"""
app
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)

@app.errorhandler(404)
def handle_error(error):
    """handle errors"""

    return jsonify({"error": "Not found", }), 404

@app.teardown_appcontext
def teardown_appcontext(self):
    """
    calls storage.close(
    """
    storage.close()





if __name__ == "__main__":
    a = getenv("HBNB_API_HOST ", default='0.0.0.0')
    b = getenv('HBNB_API_PORT', default=5000)
    app.run(host=a, port=b, threaded=True)
