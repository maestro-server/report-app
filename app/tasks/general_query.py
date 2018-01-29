import requests, json
from app import celery
from .upload_json import task_upload
from app.libs.url import FactoryURL


@celery.task(name="qgeneral.api", bind=True)
def task_qgeneral(self, type, filters):
    type = type.lower()

    path = FactoryURL.make(path=type)
    query = json.dumps(filters)
    context = requests.post(path, json={'query': query, 'limit': 99999})

    if context.status_code is 200:
        result = context.json()
        if result['found'] > 0:
            insert_id = task_upload('general', result['items'])

        #return {'name': self.request.task, 'upload-id': insert_id}