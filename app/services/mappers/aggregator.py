
from app.services.aggregator.aggrDict import AggrDict
from app.services.aggregator.aggrListObj import AggrListObj
from app.services.aggregator.aggrImmutable import AggrImmutable

def mapperA():
    return [
        AggrImmutable("family"),
        AggrImmutable("size"),
        AggrImmutable("provider"),
        AggrDict("datacenters", sub="name"),
        AggrDict("datacenters", sub="provider"),
        AggrDict("datacenters", sub="instance"),
        AggrDict("datacenters", sub="region"),
        AggrDict("os", sub="base", aggrk="base"),
        AggrListObj("regions"),
        AggrListObj("zones"),
        AggrListObj("deps", sub="name"),
        AggrListObj("services", sub="name"),
        AggrListObj("deploy", sub="type"),
        AggrListObj("contacts", sub="channel"),
        AggrListObj("applications", sub="name"),
        AggrListObj("system", sub="name"),
        AggrListObj("clients", sub="name"),
        AggrListObj("entry", sub="name"),
        AggrListObj("auth", sub="type"),
        AggrListObj("tags", sub="key"),
    ]