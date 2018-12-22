import os
import json
from math import ceil
from flask import request
from flask_restful import Resource
from pydash import defaults, has

from app.repository.model import Model
from app.services.filter import FilterAPI
from app.repository.reports import Reports
from app.services.privateAuth import private_auth


class ReportSingleApp(Resource):
    @private_auth
    def get(self, table_name):
        """
        @api {get} /reports/<table_name>/ Get Table Data
        @apiName GetTableData
        @apiGroup Reports

        @apiParam(Param) {String} table_name Table Name

        @apiSuccessExample {json} Success-Response:
                HTTP/1.1 200 OK
                 [{
                    "limit": <int>,
                    "total_pages": <int>,
                    "found": <int>,
                    "page": <int>,
                    "items": []
                 }]
        """
        Report = Reports(table_name)
        req = request.args.to_dict()

        pagination = defaults(req, {'limit': os.environ.get("MAESTRO_REPORT_RESULT_QTD", 1500), 'page': 1,
                                    'orderBy': 'updated_at', 'ascending': -1})
        limit = int(pagination['limit'])
        page = int(pagination['page'])
        skip = (page - 1) * limit
        direction = 1 if int(pagination['ascending']) else -1
        orderBy = pagination['orderBy']

        query = {}
        if has(req, 'query'):
            query = json.loads(req['query'])

        args = FilterAPI() \
            .addBatchFilters(query) \
            .make()

        count = Report.count(args)
        return {
            'found': count,
            'total_pages': ceil(count / limit),
            'page': page,
            'limit': limit,
            'items': Report.getAll(args, limit, skip, orderBy, direction)
        }

    @private_auth
    def delete(self, table_name):
        """
        @api {delete} /reports/<table_name>/ Delete Table Data
        @apiName DeleteTableData
        @apiGroup Reports

        @apiParam(Param) {String} table_name Table Name

        @apiSuccessExample {json} Success-Response:
                HTTP/1.1 204
                 {}
        """
        try:
            data = Model().deleteCollection(table_name)
        except Exception as error:
            return str(error), 502

        if int(data['ok']) == 0:
            return data, 400

        return data
