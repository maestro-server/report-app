
from app import db

class Model(object):
    
    def deleteCollection(self, table_name):
        if table_name:
            return db.drop_collection(table_name) 