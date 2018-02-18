
from app.views import api, app

@api.representation('text/plain')
def output_txt(data, code, headers=None):
    items = data['items']
    data = ""

    for item in items:
        row = ""
        for k, v in item.items():
            row += " - %s: %s" % (k, v)

        data += row+"\n\r"

    resp = app.make_response(data)
    return resp