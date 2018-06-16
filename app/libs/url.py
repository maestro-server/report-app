import os


class FactoryURL(object):
    @staticmethod
    def make(path="", resource="MAESTRO_DATA_URI"):
        base = os.environ.get(resource, "http://localhost:5010")

        return "%s/%s" % (base, path)


class FactoryDataURL(object):
    @staticmethod
    def make(path=""):
        return FactoryURL.make(path, "MAESTRO_DATA_URI")

class FactoryReportURL(object):
    @staticmethod
    def make(path=""):
        return FactoryURL.make(path, "MAESTRO_REPORT_URI")
