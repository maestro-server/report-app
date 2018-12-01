
from.aggr import Aggr

class AggrImmutable(Aggr):

    def aggregate(self, df):
        self._result = df.groupby(df).count()
