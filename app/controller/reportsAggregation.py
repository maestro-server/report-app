import pandas as pd
from flask import request
from flask_restful import Resource

from app.repository.reports import Reports


class ReportAggregationApp(Resource):

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

        df =  pd.DataFrame(data)

        datacenters = df['datacenters'].apply(pd.Series)


        print(datacenters.groupby('name', as_index=False).agg({"_id": "count"}))



        req = request.args.to_dict()
        return data
