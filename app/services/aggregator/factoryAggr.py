

class FactoryAggr(object):

    def __init__(self, dataframe):
        self._dataframe = dataframe

    def run(self, cls):
        field = cls.getField()

        if field in self._dataframe:
            df = self._dataframe[field]
            cls.aggregate(df)

            return cls.getResult()