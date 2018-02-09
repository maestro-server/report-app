import datetime
from app import db
from bson.objectid import ObjectId
from pymongo import InsertOne
from app.error.missingError import MissingError
from pymongo.errors import BulkWriteError

from pydash import omit

class Reports(object):
    def __init__(self, name=None, id=None):
        if name is None:
            name = self.__class__.__name__.lower()

        self.col = db[name]
        self.__id = id

    def getAll(self, filter = {}, limit = 10, skip = 0):
        result = self.col.find(filter)\
            .limit(limit)\
            .skip(skip)

        return list(result)

    def count(self, filter = {}):
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

    @staticmethod
    def makeObjectId(id):
        if id:
            return {'_id': Model.castObjectId(id)}

    @staticmethod
    def castObjectId(id):
        return ObjectId(id)