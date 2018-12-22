
from flask_restful import Resource
from app.libs.makeAggregation import make_aggregation
from app.repository.reports import Reports
from app.services.privateAuth import private_auth


class ReportAggregationApp(Resource):
    @private_auth
    def get(self, table_name):
        """
        @api {get} /aggregation/<table_name>/ Get Data Aggregation
        @apiName GetTableAggregation
        @apiGroup Reports

        @apiParam(Param) {String} table_name Table Name

        @apiSuccessExample {json} Success-Response:
                HTTP/1.1 200 OK
                 [{
                    "name": <int>,
                    "aggr": []
                 }]
        """
        Report = Reports(table_name)
        data = Report.getAll(limit=99999)
        aggr = make_aggregation(data)

        return {
            'name': table_name,
            'aggr': aggr
        }