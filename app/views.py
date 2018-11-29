# -*- encoding: utf-8 -*-
"""
Python Routes
Licence: GPLv3
"""

from flask_restful import Api
from app import app
from flask import jsonify

from .controller import HomeApp, GeneralReport, PivotReport, ReportsApp, ReportSingleApp, ReportAggregationApp

api = Api(app)

api.add_resource(HomeApp, '/')
api.add_resource(GeneralReport, '/reports/general')
api.add_resource(PivotReport, '/reports/pivot')
api.add_resource(ReportsApp, '/reports')
api.add_resource(ReportSingleApp, '/reports/<table_name>')
api.add_resource(ReportAggregationApp, '/aggregation/<table_name>')


@app.errorhandler(404)
def error(e):
    return jsonify({'error': 'Resource not found'}), 404
