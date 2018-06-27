import os


class FactoryURL(object):
    @staticmethod
    def make(base, path=""):
        return "%s/%s" % (base, path)


class FactoryDataURL(object):
    @staticmethod
    def make(path=""):
        base = os.environ.get("MAESTRO_DATA_URI", "http://localhost:5010")
        return FactoryURL.make(base, path)

class FactoryReportURL(object):
    @staticmethod
    def make(path=""):
        base = os.environ.get("MAESTRO_REPORT_URI", "http://localhost:5005")
        return FactoryURL.make(base, path)
