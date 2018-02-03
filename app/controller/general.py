
import json
from flask_restful import Resource
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
                #task_notification.delay(msg=str(error), status='danger')
                return str(error)

            if(prepared is not None):
                general_id = task_qgeneral.delay(valid['owner_user'], valid['type'], prepared)

                return {'filter': valid['filters'], 'general-id': str(general_id)}
