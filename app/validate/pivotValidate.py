
from flask_restful.reqparse import RequestParser

class Validate(object):


    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("filters", type=str, required=True)
        valid.add_argument("report_id", type=str, required=True, help="Must've report id")
        valid.add_argument("owner_user", type=str, required=True, help="Must've id owner")

        return valid.parse_args()