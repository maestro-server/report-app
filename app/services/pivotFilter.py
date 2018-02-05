
from app.services.factoryFilter import FactoryFilters


class PivotFilters(object):
    @staticmethod
    def factory(input = []):

        prepared = FactoryFilters.factory(input=filters)
        return prepared
