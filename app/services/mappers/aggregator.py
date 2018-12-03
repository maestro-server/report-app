
from app.services.aggregator.aggr import Aggregator

def mapperA():
    return [
        Aggregator("datacenters", lens="name"),
        Aggregator("datacenters", lens="provider"),
        Aggregator("datacenters", lens="instance"),
        Aggregator("datacenters", lens="region"),
        Aggregator("provider"),
        Aggregator("size"),

        Aggregator("servers", lens="hostname"),
        Aggregator("servers", lens="datacenters.name"),
        Aggregator("servers", lens="datacenters.provider"),
        Aggregator("servers", lens="datacenters.instance"),
        Aggregator("servers", lens="datacenters.region"),
        Aggregator("os", lens="base"),

        Aggregator("applications", lens="name"),
        Aggregator("applications", lens="family"),
        Aggregator("applications", lens="datacenters.name"),
        Aggregator("applications", lens="datacenters.provider"),
        Aggregator("family"),

        Aggregator("system", lens="name"),
        Aggregator("systems", lens="name"),
        Aggregator("systems", lens="clients", sublens="name"),

        Aggregator("clients", lens="name"),

        Aggregator("regions"),
        Aggregator("zones"),
        Aggregator("deps", sublens="name"),
        Aggregator("services", sublens="name"),
        Aggregator("deploy", sublens="type"),
        Aggregator("contacts", sublens="channel"),

        Aggregator("entry", sublens="name"),
        Aggregator("auth", sublens="type"),
        Aggregator("tags", sublens="key"),
    ]