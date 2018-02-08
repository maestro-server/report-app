
from app.services.ruler import Ruler

class FactoryFilters(object):
    @staticmethod
    def factory(input=[], prefix=''):
     
        if len(input) <= 0:
            return {}

        Rule = Ruler(prefix)
        for filter in input:
            Rule.execute(options=filter)

        return Rule.out()
