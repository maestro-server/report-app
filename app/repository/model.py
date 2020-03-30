from app import db
from bson.objectid import ObjectId


class Model(object):
    def deleteCollection(self, table_name):
        print(table_name)
        if table_name:
            return db.drop_collection(table_name)

    @staticmethod
    def makeObjectId(id):
        if id:
            return {'_id': Model.castObjectId(id)}

    @staticmethod
    def castObjectId(id):
        return ObjectId(id)
