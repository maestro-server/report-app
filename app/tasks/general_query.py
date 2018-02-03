import requests, json, os
from app import celery
from .upload_json import task_upload
from app.libs.url import FactoryURL

from pydash.objects import assign


def getRules(owner_id):
    return {'active': True, 'roles._id': owner_id}


@celery.task(name="qgeneral.api", bind=True)
def task_qgeneral(self, owner_user, type, filters={}):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_DISCOVERY", 10))
    type = type.lower()

    path = FactoryURL.make(path=type)
    rules = getRules(owner_user)

    query = {**rules, **filters}
    fjson = json.dumps(query)

    context = requests.post(path, json={'query': fjson, 'limit': 99999}, timeout=timeout)

    if context.status_code is 200:
        result = context.json()
        if result['found'] > 0:
            insert_id = task_upload.delay('general', result['items'])

            return {'name': self.request.task, 'upload-id': insert_id, 'filter': fjson}
