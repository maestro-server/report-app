

from app.libs.dataFrame import DataFrame
from app.views import api, app


@api.representation('text/csv')
def output_csv(data, code, headers=None):
    result = DataFrame(data['items']).factoryCSV()

    resp = app.make_response(result.output())
    return resp