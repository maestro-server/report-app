

from app.views import api, app

@api.representation('text/inventory')
def output_inventory(data, code, headers=None):

    data = 'some,csv,fields'
    resp = app.make_response(data)
    return resp