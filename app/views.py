# -*- encoding: utf-8 -*-
"""
Python Routes
Licence: GPLv3
"""

from flask_restful import Api
from app import app
from flask import jsonify

from .controller import *

api = Api(app)

api.add_resource(ReportsApp, '/')
api.add_resource(GeneralReport, '/general')
api.add_resource(PivotReport, '/pivot')



@app.errorhandler(404)
def error(e):
    return jsonify({'error': 'Resource not found'})