import datetime
from pymongo import InsertOne
from pymongo.errors import BulkWriteError
from pydash import omit
from app import db
from app.repository.model import Model


class Reports(object):
    def __init__(self, name=None, id=None):
        if name is None:
            name = self.__class__.__name__.lower()

        self.col = db[name]
        self.__id = id

    def getAll(self, filter={}, limit=10, skip=0, orderBy='updated_at', direction=-1):
        result = self.col.find(filter) \
            .sort(orderBy, direction) \
            .limit(limit) \
            .skip(skip)

        return list(result)

    def count(self, filter={}):
        return self.col.count(filter)

    def get(self):
        return self.col.find_one(Model.makeObjectId(self.__id))

    def batch_process(self, data):
        requests = []
        for item in data:
            cal = InsertOne(omit(item['data'], '_id'))
            requests.append(cal)

        try:
            result = self.col.bulk_write(requests)
            return result.bulk_api_result
        except BulkWriteError as bwe:
            return bwe.details

    def makeDateAt(self, key):
        return {key: datetime.datetime.utcnow()}
