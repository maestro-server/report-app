import sys
import pandas as pd
from app.services.aggregator.factoryAggr import FactoryAggr
from app.services.mappers.aggregator import mapperA


def view_label(result):
    return {
        'label': result.index.tolist(),
        'data': result.tolist()
    }


def view_dict(result):
    return result.to_dict()


def make_aggregation(data, view='dict', type=None):
    aggr = {}

    df = pd.DataFrame(data)
    factory = FactoryAggr(df, type)

    for mapp in mapperA():
        result = factory.run(mapp)

        if isinstance(result, pd.Series) and len(result) > 0:
            entity = mapp.uniqueField()

            mth = "view_%s" % view
            aggr[entity] = {
                'aggr': getattr(sys.modules[__name__], mth)(result),
                'opts': mapp.getOpts()
            }

    return aggr
