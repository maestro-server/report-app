import io
import csv
import pandas as pd
from pydash import get
from pandas.io.json import json_normalize

from app.services.mappers.columns_header import mapperH


class DataFrame:
    def __init__(self, items, normalize=True):
        self.__result = None
        self.__output = io.StringIO()

        dt = json_normalize(items) if normalize else items
        self.__dt = pd.DataFrame(dt)

    def factoryCSV(self):
        self.__result = self.__dt.to_csv(self.__output, sep=',', quoting=csv.QUOTE_NONNUMERIC)
        return self

    def getHeaders(self):
        listed = list(self.__dt.dropna(axis=1, how='all'))
        return sorted(listed, key=lambda it: get(mapperH(), it, 50))

    def output(self):
        return self.__output.getvalue()
