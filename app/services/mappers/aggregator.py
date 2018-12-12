
from app.services.aggregator.aggr import Aggregator

def mapperA():
    return [
        Aggregator("datacenters", lens="provider", opts={'ct': 'doughnut', 'txt': 'Providers'}),
        Aggregator("provider", opts={'ct': 'doughnut', 'txt': 'Providers'}),
        Aggregator("servers", lens="datacenters.provider", opts={'ct': 'doughnut', 'txt': 'Providers (by Servers)'}),
        Aggregator("applications", lens="datacenters.provider", sublens="datacenters,provider", opts={'ct': 'doughnut', 'txt': 'Providers (by Apps)'}),

        Aggregator("datacenters", lens="name", opts={'ct': 'polar', 'txt': 'Datacenters'}),
        Aggregator("servers", lens="datacenters.name", opts={'ct': 'polar', 'txt': 'Datacenters (by Servers)'}),
        Aggregator("applications", lens="datacenters.name", sublens="datacenters.name", opts={'ct': 'polar', 'txt': 'Datacenters (by Apps)'}),

        Aggregator("servers", lens="datacenters.region", opts={'ct': 'doughnut', 'txt': 'Regions (by Servers)'}),
        Aggregator("datacenters", lens="region", opts={'ct': 'doughnut', 'txt': 'Regions'}),
        Aggregator("regions", opts={'ct': 'doughnut', 'txt': 'Regions'}),

        Aggregator("datacenters", lens="zone", include=['servers'], opts={'ct': 'doughnut', 'txt': 'Zones'}),
        Aggregator("zones", opts={'ct': 'doughnut', 'txt': 'Zones'}),

        Aggregator("servers", lens="hostname", opts={'ct': 'total', 'txt': 'Hostname', 'limit': 12}),

        Aggregator("datacenters", lens="instance", opts={'ct': 'bar', 'txt': 'Instances', 'size': 'col-sm-8', 'legend': False, 'limit': 16}),
        Aggregator("servers", lens="datacenters.instance", opts={'ct': 'bar', 'txt': 'Instances (by Servers)', 'size': 'col-sm-8', 'legend': False, 'limit': 16}),

        Aggregator("size", opts={'ct': 'bar', 'txt': 'Size', 'size': 'col-sm-8', 'legend': False}),

        Aggregator("family", opts={'ct': 'pie', 'txt': 'Family'}),
        Aggregator("applications", lens="family", sublens="family",
                   opts={'ct': 'pie', 'txt': 'Family (by Apps)'}),

        Aggregator("applications", lens="name", sublens="name", opts={'ct': 'bar', 'txt': 'Apps', 'size': 'col-sm-8', 'legend': False}),

        Aggregator("servers", lens="os.base", sublens="base", opts={'ct': 'pie', 'txt': 'OS (by Servers)'}),

        Aggregator("system", lens="name", sublens="name", opts={'ct': 'bar', 'txt': 'Systems', 'size': 'col-sm-8', 'legend': False}),
        Aggregator("systems", lens="name", opts={'ct': 'bar', 'txt': 'Systems', 'size': 'col-sm-8', 'legend': False}),

        Aggregator("deps", sublens="name", opts={'ct': 'pie', 'txt': 'Most dependencies apps'}),
        Aggregator("services", sublens="name", opts={'ct': 'pie', 'txt': 'Services'}),
        Aggregator("os", lens="base", opts={'ct': 'pie', 'txt': 'OS'}),
        Aggregator("deploy", sublens="type", opts={'ct': 'polar', 'txt': 'Deploy'}),
        Aggregator("contacts", sublens="channel", opts={'ct': 'doughnut', 'txt': 'Contacts'}),

        Aggregator("entry", sublens="name", opts={'ct': 'pie', 'txt': 'Endpoint Apps'}),
        Aggregator("auth", sublens="type", opts={'ct': 'polar', 'txt': 'Auths'}),

        Aggregator("systems", lens="clients", sublens="name", opts={'ct': 'bar', 'txt': 'Clients', 'size': 'col-sm-8', 'legend': False}),
        Aggregator("clients", lens="name", sublens="name", opts={'ct': 'bar', 'txt': 'Clients', 'size': 'col-sm-8', 'legend': False}),


        Aggregator("tags", sublens="key", opts={'ct': 'total', 'txt': 'Tags', 'limit': 12}),
    ]