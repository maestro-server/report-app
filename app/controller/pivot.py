
from flask_restful import Resource
from app.validate.pivotValidate import Validate
from app.repository import Reports

class PivotReport(Resource):
    def get(self):
        return Reports().getAll()

    def post(self, instance):
        valid = Validate().validate()

        if valid:
            Report = Reports(instance)

        return valid