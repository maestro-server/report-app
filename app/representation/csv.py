
from app.views import api, app


@api.representation('text/csv')
def output_csv(data, code, headers=None):
    items = data['items']

    with open('test.csv', 'w') as f:
        f.write('Application Name, Application ID\n')
        for key in items.keys():
            f.write("%s,%s\n" % (key, items[key]))

    data = 'some,csv,fields'
    resp = app.make_response(data)
    return resp
