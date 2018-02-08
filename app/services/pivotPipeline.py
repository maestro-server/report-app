
import copy, json
from app.services.factoryFilter import FactoryFilters
from app.libs.factoryOwnerRule import getRules

from pydash import get


class PivotPipeline(object):
    @staticmethod
    def factory(input, owner_id):
        mapper = PivotPipeline.mapper()

        prepared = []
        prev = ''
        for key, item in input.items():
            if item['enabled'] == True:

                # needb jump first lookup
                if len(prepared) > 0 and key in mapper:
                    lookup = PivotPipeline.facLookup(key, mapper, prev)

                    prepared.append(lookup)
                    prepared.append({"$unwind": get(mapper, '%s.unwind' % key)})
                    prev = key

                # matches
                if key in mapper:
                    match = PivotPipeline.facMatch(item['filters'], owner_id, prev)
                    prepared.append({'$match': match})

               
        return prepared

    @staticmethod
    def mapper():
        query = {
            "clients": {},
            "systems": {
                "localField": "{prev}_id",
                "foreignField": "clients._id",
                "unwind": {"path": "$systems", "preserveNullAndEmptyArrays": True}
            },
            "applications": {
                "localField": "{prev}_id",
                "foreignField": "system._id",
                "unwind": {"path": '$applications', "includeArrayIndex": 'servers', "preserveNullAndEmptyArrays": True}
            },
            "servers": {
                "localField": "{prev}servers",
                "foreignField": "_id",
                "unwind": {"path": "$servers", "preserveNullAndEmptyArrays": True}
            }
        }
        return query

    @staticmethod
    def facLookup(key, mapper, prev=''):
        if prev:
            prev = '%s.' % prev

        return {
            "$lookup": {
                "from": key,
                "localField": get(mapper, '%s.localField' % key).replace('{prev}', prev),
                "foreignField": get(mapper, '%s.foreignField' % key),
                "as": key
            }
        }


    @staticmethod
    def facMatch(filters, owner_id, prefix):
        ruler = getRules(owner_id, prefix)

        match = copy.copy(ruler)
        ff = FactoryFilters.factory(input=filters, prefix=prefix)
        if ff:
            match.update(ff)

        return match