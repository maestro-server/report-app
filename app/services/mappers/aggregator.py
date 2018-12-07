
from app.services.aggregator.aggr import Aggregator

def mapperA():
    return [
        Aggregator("datacenters", lens="name", opts={'ct': 'polar', 'txt': 'Datacenters'}),
        Aggregator("datacenters", lens="provider", opts={'ct': 'polar', 'txt': 'Providers'}),
        Aggregator("datacenters", lens="instance", opts={'ct': 'bar', 'txt': 'Instances', 'size': 'col-sm-8', 'legend': False, 'limit': 16}),
        Aggregator("datacenters", lens="region", opts={'ct': 'doughnut', 'txt': 'Regions'}),
        Aggregator("datacenters", lens="zone", include=['servers'], opts={'ct': 'doughnut', 'txt': 'Zones'}),
        Aggregator("provider", opts={'ct': 'polar', 'txt': 'Providers'}),
        Aggregator("size", opts={'ct': 'bar', 'txt': 'Size', 'size': 'col-sm-8', 'legend': False}),

        Aggregator("servers", lens="hostname", opts={'ct': 'table', 'txt': 'Hostname'}),
        Aggregator("servers", lens="datacenters.name", opts={'ct': 'polar', 'txt': 'Datacenters'}),
        Aggregator("servers", lens="datacenters.provider", opts={'ct': 'polar', 'txt': 'Providers'}),
        Aggregator("servers", lens="datacenters.instance", opts={'ct': 'bar', 'txt': 'Instances', 'size': 'col-sm-8', 'legend': False, 'limit': 16}),
        Aggregator("servers", lens="datacenters.region", opts={'ct': 'doughnut', 'txt': 'Regions'}),
        Aggregator("os", lens="base"),

        Aggregator("applications", lens="name", opts={'ct': 'table', 'txt': 'Apps'}),
        Aggregator("applications", lens="family", opts={'ct': 'pie', 'txt': 'Family'}),
        Aggregator("applications", lens="datacenters.name", opts={'ct': 'polar', 'txt': 'Datacenters'}),
        Aggregator("applications", lens="datacenters.provider", opts={'ct': 'polar', 'txt': 'Providers'}),
        Aggregator("family"),

        Aggregator("system", lens="name", opts={'ct': 'table', 'txt': 'Systems'}),
        Aggregator("systems", lens="name", opts={'ct': 'table', 'txt': 'Systems'}),
        Aggregator("systems", lens="clients", sublens="name", opts={'ct': 'table', 'txt': 'Clients'}),

        Aggregator("clients", lens="name", opts={'ct': 'table', 'txt': 'Clients'}),

        Aggregator("regions", opts={'ct': 'doughnut', 'txt': 'Regions'}),
        Aggregator("zones", opts={'ct': 'doughnut', 'txt': 'Zones'}),
        Aggregator("deps", sublens="name", opts={'ct': 'pie', 'txt': 'Dependencies'}),
        Aggregator("services", sublens="name", opts={'ct': 'pie', 'txt': 'Services'}),
        Aggregator("deploy", sublens="type", opts={'ct': 'polar', 'txt': 'Deploy'}),
        Aggregator("contacts", sublens="channel", opts={'ct': 'doughnut', 'txt': 'Contacts'}),

        Aggregator("entry", sublens="name", opts={'ct': 'pie', 'txt': 'Endpoints'}),
        Aggregator("auth", sublens="type", opts={'ct': 'polar', 'txt': 'Auths'}),
        Aggregator("tags", sublens="key", opts={'ct': 'table', 'txt': 'Tags'}),
    ]