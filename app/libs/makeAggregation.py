
import pandas as pd
from app.services.aggregator.factoryAggr import FactoryAggr
from app.services.mappers.aggregator import mapperA


def make_aggregation(data):
    aggr = {}

    df = pd.DataFrame(data)
    factory = FactoryAggr(df)

    for mapp in mapperA():
        result = factory.run(mapp)

        if isinstance(result, pd.Series):
            entity = mapp.uniqueField()
            aggr[entity] = {
                'label': result.index.tolist(),
                'data': result.tolist()
            }

    return aggr