import copy
from pydash import get
from app.services.factoryFilter import FactoryFilters
from app.libs.factoryOwnerRule import getRules
from app.services.mappers.client_system_app_server import mapperI


class PivotPipeline(object):
    def __init__(self):
        self.__first = None
        self.__mapper = mapperI
        self.__result = []

    def getFirst(self):
        return self.__first

    def getResult(self):
        return self.__result

    def hasResult(self):
        return self.getResult() is not None

    def factory(self, input, owner_id):
        mapp = self.__mapper()

        prev = ''
        prepared = []
        for key, item in input.items():
            if item['enabled'] is True:

                # get first element
                if len(prepared) == 0:
                    self.__first = key

                # needb jump first lookup
                if len(prepared) > 0 and key in mapp:
                    lookup = PivotPipeline.facLookup(key, mapp, prev)

                    prepared.append(lookup)
                    prepared.append({"$unwind": get(mapp, '%s.unwind' % key)})
                    prev = key

                # matches
                if key in mapp:
                    match = PivotPipeline.facMatch(item['filters'], owner_id, prev)
                    prepared.append({'$match': match})

        self.__result = prepared

    @staticmethod
    def facLookup(key, mapper, prev=''):
        if prev:
            prev = '%s.' % prev

        return {
            "$lookup": {
                "from": key,
                "localField": get(mapper, '%s.localField' % key, '').replace('{prev}', prev),
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
