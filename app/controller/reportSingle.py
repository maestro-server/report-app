
import os,json
from math import ceil
from flask import request
from flask_restful import Resource
from app.repository.model import Model

from pydash import defaults, has
from app.services.filter import FilterAPI
from app.repository.reports import Reports

class ReportSingleApp(Resource):

    def get(self, table_name):
        Report = Reports(table_name)
        req = request.args.to_dict()

        pagination = defaults(req, {'limit': os.environ.get("MAESTRO_REPORT_RESULT_QTD", 1500), 'page': 1})
        limit = int(pagination['limit'])
        page = int(pagination['page'])
        skip = (page - 1) * limit

        query={}
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
            'items': Report.getAll(args, limit, skip)
        }

    def delete(self, table_name):
        try:
            data = Model().deleteCollection(table_name)
        except Exception as error:
            return str(error), 502

        if int(data['ok']) == 0:
            return data, 400

        return data



