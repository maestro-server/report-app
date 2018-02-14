
from simplexml import dumps
from app.views import api, app

@api.representation('application/xml')
def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = app.make_response(dumps({'response' :data}))
    return resp