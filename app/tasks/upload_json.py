import datetime, uuid, requests, os
from app import celery
from app.libs.url import FactoryURL


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


@celery.task(name="uplaod.api", bind=True)
def task_upload(self, name, result):
    id = str(uuid.uuid4())
    now = datetime.datetime.now()

    colname = '%s__%s_%s' % (name, now, id)
    path = FactoryURL.make(path="reports", resource="MAESTRO_URL")

    print(len(result))

    qtd = int(os.environ.get("MAESTRO_INSERT_QTD", 500))
    for x in batch(result, qtd):
        print(len(x))

        # context = requests.post(path, json={'name': colname, 'result': result})


        # return {'name': self.request.task}
