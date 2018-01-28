
from app.services.ruler import Ruler

class FactoryFilters(object):
    @staticmethod
    def factory(input):

        Rule = Ruler()
        for filter in input:
            Rule.exec(options=filter)

        print(Rule.out())
        return Rule.out()
