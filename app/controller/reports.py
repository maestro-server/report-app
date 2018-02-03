

from flask import request
from flask_restful import Resource
from app.validate.integrityData import validate

from app.repository.reports import Reports
from app.tasks.notification import task_notification
from app.validate.webhookValidate import Validate

class ReportsApp(Resource):

    def post(self):
        valid = Validate().validate()

        if valid:
            data = request.get_json(force=True)

            format = []

            for item in data['results']:

                if validate(item):
                    format.append({
                        'data': item
                    })

            if format:
                try:
                    return Reports(data['colname']).batch_process(format)
                except Exception as error:
                    return str(error), 500
                    #task_notification.delay(msg=str(error), status='danger')


