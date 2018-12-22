from flask import request
from flask_restful import Resource

from app.libs.logger import logger

from app.repository.reports import Reports
from app.services.privateAuth import private_auth
from app.validate.webhookValidate import Validate


class ReportsApp(Resource):
    @private_auth
    def post(self):
        """
        @api {post} /reports Insert Batch Process
        @apiName PostReport
        @apiGroup Reports
        @apiDescription Clone the result on new database, used by reports worker

        @apiParam(Param) {String} colname Name of the columm
        @apiParam(Param) {Array} results Results, clone the data on new db

        @apiSuccessExample {json} Success-Response:
                HTTP/1.1 201 OK
                 {
                 }
        """
        valid = Validate().validate()

        if valid:
            data = request.get_json(force=True)

            if data:
                try:
                    return Reports(data['colname']).batch_process(data['results'])
                except Exception as error:
                    logger.error("Reports Controller [reports] - %s", str(error))
                    return str(error), 500

        return valid, 400
