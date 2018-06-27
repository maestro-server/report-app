import json
from flask_restful import Resource

from app.validate.pivotValidate import Validate
from app.services.pivotPipeline import PivotPipeline
from app.tasks.pivot_query import task_qpivot
from app.tasks.notification import task_notification


class PivotReport(Resource):
    def post(self):
        PPipeline = PivotPipeline()
        valid = Validate().validate()

        if valid:
            try:
                filters = json.loads(valid['filters'])
                PPipeline.factory(input=filters, owner_id=valid['owner_user'])
            except Exception as error:
                task_notification.delay(report_id=valid['report_id'], msg=str(error), status='error')
                return {'message': str(error)}, 501

            if PPipeline.hasResult():
                pivot_id = task_qpivot.delay(valid['report_id'], PPipeline.getFirst(),
                                             PPipeline.getResult())

                return {'filter': valid['filters'], 'pivot-id': str(pivot_id)}

        return valid, 502
