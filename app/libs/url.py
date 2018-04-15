
import os

class FactoryURL(object):

    @staticmethod
    def make(path="", resource="MAESTRO_DATA_URI"):
        base = os.environ.get(resource, "http://localhost:5005")

        return "%s/%s" % (base, path)