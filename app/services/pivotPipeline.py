
from app.services.factoryFilter import FactoryFilters


class PivotPipeline(object):
    @staticmethod
    def factory(input = []):
        
        prepared = {}
        for key, item in input.items():
            if item['enabled'] == True:
                
                ff = FactoryFilters.factory(input=item['filters'])
                prepared.update({key:ff})

        return prepared

    @staticmethod
    def mapper(input = []):
        query = {
                    "system": {
                        "localField": "_id",
                        "foreignField": "clients._id",
                        "unwind": {path: "$system", preserveNullAndEmptyArrays: true}
                    },
                    "applications": {
                        "localField": "system._id",
                        "foreignField": "system._id",
                        "unwind":  {path: '$applications', includeArrayIndex: 'servers', preserveNullAndEmptyArrays: true}
                    },
                    "servers": {
                        "localField": "applications.servers",
                        "foreignField": "_id",
                        "unwind": {path: "$server", preserveNullAndEmptyArrays: true}
                    }
                }
        return query
        
