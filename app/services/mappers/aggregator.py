
from app.services.aggregator.aggr import Aggregator

def mapperA():
    return [
        Aggregator("datacenters", lens="provider", opts={'ct': 'doughnut', 'txt': 'Providers', 'order': 1}),
        Aggregator("provider", opts={'ct': 'doughnut', 'txt': 'Resource', 'order': 1}),
        Aggregator("servers", lens="datacenters.provider", opts={'ct': 'doughnut', 'txt': 'Providers (by Servers)', 'order': 1}),
        Aggregator("applications", lens="datacenters.provider", sublens="datacenters,provider", opts={'ct': 'doughnut', 'txt': 'Providers (by Apps)', 'order': 1}),

        Aggregator("datacenters", lens="name", opts={'ct': 'polar', 'txt': 'Datacenters', 'order': 2}),
        Aggregator("servers", lens="datacenters.name", opts={'ct': 'polar', 'txt': 'Datacenters (by Servers)', 'order': 2}),
        Aggregator("applications", lens="datacenters.name", sublens="datacenters.name", opts={'ct': 'polar', 'txt': 'Datacenters (by Apps)', 'order': 2}),

        Aggregator("servers", lens="datacenters.region", opts={'ct': 'doughnut', 'txt': 'Regions (by Servers)', 'order': 3}),
        Aggregator("datacenters", lens="region", opts={'ct': 'doughnut', 'txt': 'Regions', 'order': 3}),
        Aggregator("regions", opts={'ct': 'doughnut', 'txt': 'Regions', 'order': 3}),

        Aggregator("datacenters", lens="zone", include=['servers'], opts={'ct': 'doughnut', 'txt': 'Zones', 'order': 4}),
        Aggregator("zones", opts={'ct': 'doughnut', 'txt': 'Zones', 'order': 4}),

        Aggregator("servers", lens="hostname", opts={'ct': 'total', 'txt': 'Hostname', 'limit': 12, 'order': 5}),

        Aggregator("datacenters", lens="instance", opts={'ct': 'bar', 'txt': 'Instances', 'size': 'col-sm-8', 'legend': False, 'limit': 16, 'order': 6}),
        Aggregator("servers", lens="datacenters.instance", opts={'ct': 'bar', 'txt': 'Instances (by Servers)', 'size': 'col-sm-8', 'legend': False, 'limit': 16, 'order': 6}),

        Aggregator("size", opts={'ct': 'bar', 'txt': 'Size', 'size': 'col-sm-8', 'legend': False, 'order': 7}),

        Aggregator("family", opts={'ct': 'pie', 'txt': 'Family', 'order': 8}),
        Aggregator("applications", lens="family", sublens="family",
                   opts={'ct': 'pie', 'txt': 'Family (by Apps)', 'order': 8}),

        Aggregator("applications", lens="name", sublens="name", opts={'ct': 'bar', 'txt': 'Apps', 'size': 'col-sm-8', 'legend': False, 'order': 9}),

        Aggregator("servers", lens="os.base", sublens="base", opts={'ct': 'pie', 'txt': 'OS (by Servers)', 'order': 9}),
        Aggregator("os", lens="base", opts={'ct': 'pie', 'txt': 'OS', 'order': 9}),

        Aggregator("system", lens="name", sublens="name", opts={'ct': 'bar', 'txt': 'Systems', 'size': 'col-sm-8', 'legend': False, 'order': 10}),
        Aggregator("systems", lens="name", opts={'ct': 'bar', 'txt': 'Systems', 'size': 'col-sm-8', 'legend': False, 'order': 10}),

        Aggregator("deps", sublens="name", opts={'ct': 'pie', 'txt': 'Most dependencies apps', 'order': 11}),
        Aggregator("services", sublens="name", opts={'ct': 'pie', 'txt': 'Services', 'order': 12}),
        
        Aggregator("deploy", sublens="type", opts={'ct': 'polar', 'txt': 'Deploy', 'order': 13}),
        Aggregator("contacts", sublens="channel", opts={'ct': 'doughnut', 'txt': 'Contacts', 'order': 14}),

        Aggregator("entry", sublens="name", opts={'ct': 'pie', 'txt': 'Endpoint Apps', 'order': 15}),
        Aggregator("auth", sublens="type", opts={'ct': 'polar', 'txt': 'Auths', 'order': 15}),

        Aggregator("systems", lens="clients", sublens="name", opts={'ct': 'bar', 'txt': 'Clients', 'size': 'col-sm-8', 'legend': False, 'order': 16}),
        Aggregator("clients", lens="name", sublens="name", opts={'ct': 'bar', 'txt': 'Clients', 'size': 'col-sm-8', 'legend': False, 'order': 16}),

        Aggregator("tags", sublens="key", opts={'ct': 'total', 'txt': 'Tags', 'limit': 12, 'order': 17}),

        Aggregator("active", opts={'ct': 'pie', 'txt': 'Active', 'limit': 12, 'order': 18}),

        Aggregator("roles", sublens="refs", opts={'ct': 'total', 'txt': 'Access Refs', 'limit': 12, 'order': 19})
    ]