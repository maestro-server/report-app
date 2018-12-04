
from app.services.aggregator.aggr import Aggregator

def mapperA():
    return [
        Aggregator("datacenters", lens="name"),
        Aggregator("datacenters", lens="provider", opts={'ct': 'pie', 'txt': 'Providers'}),
        Aggregator("datacenters", lens="instance", opts={'ct': 'bar', 'txt': 'Instances'}),
        Aggregator("datacenters", lens="region", opts={'ct': 'pie', 'txt': 'Regions'}),
        Aggregator("datacenters", lens="zone", include=['servers'], opts={'ct': 'doughnut', 'txt': 'Zones'}),
        Aggregator("provider", opts={'ct': 'pie', 'txt': 'Providers'}),
        Aggregator("size", opts={'ct': 'pie', 'txt': 'Size'}),

        Aggregator("servers", lens="hostname"),
        Aggregator("servers", lens="datacenters.name"),
        Aggregator("servers", lens="datacenters.provider", opts={'ct': 'pie', 'txt': 'Providers'}),
        Aggregator("servers", lens="datacenters.instance", opts={'ct': 'bar', 'txt': 'Instances'}),
        Aggregator("servers", lens="datacenters.region", opts={'ct': 'doughnut', 'txt': 'Regions'}),
        Aggregator("os", lens="base"),

        Aggregator("applications", lens="name", opts={'ct': 'table', 'txt': 'Apps'}),
        Aggregator("applications", lens="family", opts={'ct': 'pie', 'txt': 'Family'}),
        Aggregator("applications", lens="datacenters.name", opts={'ct': 'doughnut', 'txt': 'Datacenters'}),
        Aggregator("applications", lens="datacenters.provider", opts={'ct': 'pie', 'txt': 'Providers'}),
        Aggregator("family"),

        Aggregator("system", lens="name", opts={'ct': 'table', 'txt': 'Systems'}),
        Aggregator("systems", lens="name", opts={'ct': 'table', 'txt': 'Systems'}),
        Aggregator("systems", lens="clients", sublens="name", opts={'ct': 'table', 'txt': 'Clients'}),

        Aggregator("clients", lens="name", opts={'ct': 'table', 'txt': 'Clients'}),

        Aggregator("regions", opts={'ct': 'doughnut', 'txt': 'Regions'}),
        Aggregator("zones", opts={'ct': 'doughnut', 'txt': 'Zones'}),
        Aggregator("deps", sublens="name", opts={'ct': 'pie', 'txt': 'Dependencies'}),
        Aggregator("services", sublens="name", opts={'ct': 'pie', 'txt': 'Services'}),
        Aggregator("deploy", sublens="type", opts={'ct': 'doughnut', 'txt': 'Deploy'}),
        Aggregator("contacts", sublens="channel", opts={'ct': 'doughnut', 'txt': 'Contacts'}),

        Aggregator("entry", sublens="name", opts={'ct': 'pie', 'txt': 'Endpoints'}),
        Aggregator("auth", sublens="type", opts={'ct': 'doughnut', 'txt': 'Auths'}),
        Aggregator("tags", sublens="key", opts={'ct': 'tables', 'txt': 'Tags'}),
    ]