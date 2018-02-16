
import io, csv, json
import pandas as pd
from pandas.io.json import json_normalize

class DataFrame:
    def __init__(self, items):
        self.__result = None
        self.__output = io.StringIO()

        dt = json_normalize(items)
        self.__dt = pd.DataFrame(dt)

    def factoryCSV(self):
        self.__result = self.__dt.to_csv(self.__output, sep=',', quoting=csv.QUOTE_NONNUMERIC)
        return self

    def getHeaders(self):
        return list(self.__result)

    def output(self):
        return self.__output.getvalue()