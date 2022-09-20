#!/usr/bin/python3
"""RESTful API AirBnB Clone"""
from models import storage
from api.vi.views import app_views
from flask import Flask, jsonify, make_response
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def storage_close(self):
    """handles @app.teardown_appcontext which calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors not found and returns a JSON - format 404"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=getenv('HBNB_API_PORT', '5000'), threaded=True)
