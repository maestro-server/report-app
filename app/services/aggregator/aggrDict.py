import pandas as pd
from.aggr import Aggr

class AggrDict(Aggr):

    def __init__(self, field,  sub="name", aggrk="_id", aggr="count"):
        self._aggr = aggr
        self._aggrk = aggrk
        super().__init__(field, sub)

    def aggregate(self, df):
        dic = df.dropna().apply(pd.Series)

        if self._sub in dic:
            aggr = dic.groupby(self._sub).agg({self._aggrk: self._aggr})
            self._result = aggr.get(self._aggrk)
