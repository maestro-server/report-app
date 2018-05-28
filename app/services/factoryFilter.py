from app.services.rules.aggregation import AggregationRuler


class FactoryFilters(object):
    @staticmethod
    def factory(input=[], prefix=''):

        if len(input) <= 0:
            return {}

        Rule = AggregationRuler(prefix)
        for filter in input:
            Rule.execute(options=filter)

        return Rule.out()
