from flask_restful.reqparse import RequestParser

class Validate(object):


    def validate(self):
        valid = RequestParser(bundle_errors=True)
        valid.add_argument("colname", type=str, required=True)
        valid.add_argument("results", type=str, required=True)

        return valid.parse_args()