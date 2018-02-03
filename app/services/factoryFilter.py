
from app.services.ruler import Ruler

class FactoryFilters(object):
    @staticmethod
    def factory(input = []):

        if len(input) <= 0:
            return {}

        Rule = Ruler()
        for filter in input:
            Rule.exec(options=filter)

        return Rule.out()
