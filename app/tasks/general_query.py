import requests, json, os
from app import celery
from .upload_json import task_upload
from app.libs.url import FactoryURL
from app.libs.factoryOwnerRule import getRules

from pydash import has

from app.tasks.notification import task_notification

@celery.task(name="qgeneral.api", bind=True)
def task_qgeneral(self, owner_user, report_id, type, filters={}):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_DATA", 10))
    type = type.lower()

    path = FactoryURL.make(path=type, resource="MAESTRO_URL")
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

    if context.status_code in [400, 403, 404, 500, 501, 502, 503]:
        notification_id = task_notification.delay(report_id=report_id, msg=context.text, status='error')
        return {'name': self.request.task, 'notification-id': str(notification_id)}