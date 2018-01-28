
import os

class FactoryURL(object):

    @staticmethod
    def make(path=""):
        base = os.environ.get("MAESTRO_DISCOVERY_URL", "http://localhost")

        return "%s/%s" % (base, path)