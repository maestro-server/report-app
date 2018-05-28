
import json
from flask_restful import Resource

from app.libs.logger import logger
from app.services.factoryFilter import FactoryFilters
from app.validate.generalValidate import Validate
from app.tasks.general_query import task_qgeneral
from app.tasks.notification import task_notification

class GeneralReport(Resource):
    def post(self):
        valid = Validate().validate()

        if valid:
            prepared = None
            try:
                filters = json.loads(valid['filters'])
                prepared = FactoryFilters.factory(input=filters)
            except Exception as error:
                task_notification.delay(report_id=valid['report_id'], msg=str(error), status='error')
                logger.error("Report: Task [general] - %s", error)
                return {'message': str(error)}, 501

            if(prepared is not None):
                general_id = task_qgeneral.delay(valid['owner_user'], valid['report_id'], valid['component'], prepared)

                return {'filter': valid['filters'], 'general-id': str(general_id)}

        return valid, 502
