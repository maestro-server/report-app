import requests
import json
import os
from pydash import has
from app import celery
from .upload_json import task_upload
from app.libs.url import FactoryDataURL
from app.libs.factoryOwnerRule import getRules
from app.tasks.notification import task_notification
import app.libs.statusCode


@celery.task(name="qgeneral.api", bind=True)
def task_qgeneral(self, owner_user, report_id, type, filters={}):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_DATA", 10))
    type = type.lower()

    path = FactoryDataURL.make(path=type)
    rules = getRules(owner_user)

    query = {**rules, **filters}
    fjson = json.dumps(query)
    context = requests.post(path, json={'query': fjson, 'limit': 99999}, timeout=timeout)

    if context.status_code is 200:
        result = context.json()
        if has(result, 'found') and result['found'] > 0:
            insert_id = task_upload.delay(report_id, 'general', result['items'])

            return {'name': self.request.task, 'upload-id': insert_id}

        task_notification.delay(report_id=report_id, msg="This report is empty", status='warning')

    if check_status(context):
        return notify_error(self.request.tas, report_id, context.text)