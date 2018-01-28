from flask_restful.reqparse import RequestParser

class Validate(object):


    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("filters", type=str, required=True)
        valid.add_argument("type", type=str, required=True)

        return valid.parse_args()