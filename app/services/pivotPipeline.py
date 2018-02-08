
import copy, json
from app.services.factoryFilter import FactoryFilters
from app.libs.factoryOwnerRule import getRules

from pydash import get


class PivotPipeline(object):
    @staticmethod
    def factory(input, owner_id):
        mapper = PivotPipeline.mapper()
        ruler = getRules(owner_id)

        prepared = []
        for key, item in input.items():
            if item['enabled'] == True:

                # needb jump first lookup
                if len(prepared) > 0 and key in mapper:
                    lookup = PivotPipeline.facLookup(key, mapper)

                    prepared.append(lookup)
                    prepared.append({"$unwind": get(mapper, '%s.unwind' % key)})

                # matches
                match = PivotPipeline.facMatch(item['filters'], ruler)
                prepared.append({'$match': match})

        return prepared

    @staticmethod
    def mapper():
        query = {
            "system": {
                "localField": "_id",
                "foreignField": "clients._id",
                "unwind": {"path": "$system", "preserveNullAndEmptyArrays": True}
            },
            "applications": {
                "localField": "system._id",
                "foreignField": "system._id",
                "unwind": {"path": '$applications', "includeArrayIndex": 'servers', "preserveNullAndEmptyArrays": True}
            },
            "servers": {
                "localField": "applications.servers",
                "foreignField": "_id",
                "unwind": {"path": "$server", "preserveNullAndEmptyArrays": True}
            }
        }
        return query

    @staticmethod
    def facLookup(key, mapper):
        return {
            "$lookup": {
                "from": key,
                "localField": get(mapper, '%s.localField' % key),
                "foreignField": get(mapper, '%s.foreignField' % key),
                "as": key
            }
        }


    @staticmethod
    def facMatch(filters, ruler):
        match = copy.copy(ruler)
        ff = FactoryFilters.factory(input=filters)
        if ff:
            match.update(ff)

        return match