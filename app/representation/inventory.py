from app.views import api, app
from app.libs.inventory import Inventory


@api.representation('text/inventory')
def output_inventory(data, code, headers=None):
    rpt = []

    result = '[all]\n\r'

    for item in data['items']:
        ansible = Inventory(item).maker()

        if ansible.getId() not in rpt:
            result += ansible.output() + '\n'
            rpt.append(ansible.getId())

    resp = app.make_response(result)
    return resp
