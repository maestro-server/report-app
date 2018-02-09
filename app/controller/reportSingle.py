

from flask_restful import Resource
from app.validate.integrityData import validate
from app.repository.model import Model

from app.repository.reports import Reports
from app.tasks.notification import task_notification
from app.validate.webhookValidate import Validate

class ReportSingleApp(Resource):

    def delete(self, table_name):
        try:
            data = Model().deleteCollection(table_name)
        except Exception as error:
            return str(error), 502

        if int(data['ok']) == 0:
            return data, 400

        return data



