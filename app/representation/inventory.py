

from app.views import api, app
from app.libs.inventory import Inventory
from pydash import get

@api.representation('text/inventory')
def output_inventory(data, code, headers=None):
    result = '[all]\n\r'

    for item in data['items']:
        ansible = Inventory(item).maker()
        result += '%s %s\n\r' % (get(item, 'hostname', ''), ansible.output())

    resp = app.make_response(result)
    return resp