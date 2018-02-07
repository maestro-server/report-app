
import json
from flask_restful import Resource
from app.validate.pivotValidate import Validate
from app.services.pivotPipeline import PivotPipeline

from app.tasks.pivot_query import task_qpivot
from app.tasks.notification import task_notification

class PivotReport(Resource):
    def post(self):
        valid = Validate().validate()

        if valid:
            prepared = None

            try:
                filters = json.loads(valid['filters'])
                prepared = PivotPipeline.factory(input=filters)
            except Exception as error:
                #task_notification.delay(report_id=valid['report_id'], msg=str(error), status='error')
                return {'message': str(error)}, 501

            if(prepared is not None):
                pivot_id = task_qpivot(valid['owner_user'], valid['report_id'], prepared)

                #return {'filter': valid['filters'], 'pivot-id': str(pivot_id)}

        return valid, 502