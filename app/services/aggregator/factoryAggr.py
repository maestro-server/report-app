

class FactoryAggr(object):

    def __init__(self, dataframe, type):
        self._dataframe = dataframe
        self._type = type

    def run(self, cls):
        field = cls.getField()

        if field in self._dataframe:
            df = self._dataframe[field]
            cls.execute(df, self._type)
            return cls.getResult()