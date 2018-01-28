import requests, json
from app import celery
from .upload_json import task_upload
from app.libs.url import FactoryURL


@celery.task(name="qgeneral.api", bind=True)
def task_qgeneral(self, type, filters):
    type = type.lower()

    path = FactoryURL.make(path=type)
    query = json.dumps(filters)
    context = requests.post(path, json={'query': query})

    print(context.status_code)

    if context.status_code is 200:
        result = context.json()
        return result

    # insert_id = task_upload.delay(result)

    # return {'name': self.request.task, 'insert-id': insert_id}
