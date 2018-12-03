import pandas as pd
from pydash.objects import get


class Aggregator(object):
    def __init__(self, field, lens=None, sublens='_id'):
        self._field = field
        self._lens = lens
        self._sublens = sublens

        self._result = []
        self._transf = []
        self._df = None

    def aggregate(self, df):

        self._tmp_dataframe = df \
            .dropna() \
            .apply(self.transformData)

        if "stack" in self._transf:
            self._tmp_dataframe = self._tmp_dataframe.stack() \
                .reset_index(level=1, drop=True)

        self.groupCount()

    def groupAggrCount(self):
        self._result = self._tmp_dataframe \
            .groupby(self._sub) \
            .agg({self._aggrk: self._aggr}) \
            .get(self._aggrk)

    def groupCount(self):
        self._result = self._tmp_dataframe \
            .groupby(self._tmp_dataframe) \
            .count()

    def transformData(self, data):

        if isinstance(data, dict):
            data = get(data, self._lens)

        if isinstance(data, list):
            self._transf.append("stack")
            data = map(self.reducev, data)
            return pd.Series(data)

        return data

    def reducev(self, data):

        if isinstance(data, dict):
            return get(data, self._sublens)

        return data

    def getField(self):
        return self._field

    def uniqueField(self):
        arr = [self._field]
        if self._lens:
            arr += self._lens.split(".")

        return "_".join(arr)

    def getResult(self):
        return self._result
