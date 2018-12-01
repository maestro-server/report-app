
class Aggr(object):

    def __init__(self, field, sub=''):
        self._field = field
        self._sub = sub
        self._result = []

    def getField(self):
        return self._field

    def uniqueField(self):
        return "%s_%s" % (self._field, self._sub)

    def getResult(self):
        return self._result