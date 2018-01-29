
import os

class FactoryURL(object):

    @staticmethod
    def make(path="", resource="MAESTRO_DISCOVERY_URL"):
        base = os.environ.get(resource, "http://localhost")

        return "%s/%s" % (base, path)