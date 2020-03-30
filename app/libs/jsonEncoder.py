import json
import datetime
import pandas as pd
from bson import ObjectId


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime) or (type(obj) is pd.Timestamp):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)
