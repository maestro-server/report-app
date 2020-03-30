import json
import datetime
import pandas as pd
from bson import ObjectId


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        if (type(obj) is pd.Timestamp):
            return obj.isoformat()
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()

        try:
            return json.JSONEncoder.default(self, obj)
        except TypeError as error:
            logger.error(str(error))

