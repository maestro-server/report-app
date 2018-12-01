
import pandas as pd
from.aggr import Aggr

class AggrListObj(Aggr):

    def aggregate(self, df):

        dic = df\
            .dropna()\
            .apply(self.merged)\
            .stack()\
            .reset_index(level=1, drop=True)

        self._result = dic.groupby(dic).count()

    def merged(self, services):

        if services and isinstance(services, list):
            services = map(self.reducev, services)

        return pd.Series(services)

    def reducev(self, data):
        if isinstance(data, dict):
            return data.get(self._sub)

        if isinstance(data, (str, int, float)):
            return data