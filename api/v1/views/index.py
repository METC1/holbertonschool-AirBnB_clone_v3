#!/usr/bin/python3
"""
manages app views routes using flask and python
also uses jsonify to convert to json 
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """
    route status returns a status:OK in the JSON format
    """
    return (jsonify({'status': 'ok'}))


@app_views.route('/stats', strict_slashes=False)
def stats():
    """
    route stats returns the number of objects by type
    """
    return (jsonify({"amenities": storage.count('Amenity'),
                     "cities": storage.count('City'),
                     "places": storage.count('Place'),
                     "reviews": storage.count('Review'),
                     "states": storage.count('State'),
                     "users": storage.count('User')}))
