""" Error pages definitions """

import json
from flask import make_response, jsonify
from DeviceManager.app import app


@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({"msg": "Invalid endpoint requested"}), 404)


@app.errorhandler(500)
def internal_error(e):
    return make_response(jsonify({"msg": "Internal Error"}), 500)
