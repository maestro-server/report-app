import os
import json
import requests
from .upload_json import task_upload
from .notification import task_notification
from app import celery
from app.libs.url import FactoryDataURL
from app.libs.status_code import check_status, string_status


@celery.task(name="qpivot.api", bind=True)
def task_qpivot(self, owner_user, report_id, entity, pipeline={}):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_DATA", 10))

    path = FactoryDataURL.make("aggregate")
    jpipeline = json.dumps(pipeline)

    context = requests.post(path, json={'entity': entity, 'pipeline': jpipeline}, timeout=timeout)

    if context.status_code is 200:
        result = context.json()
        if result['items']:
            insert_id = task_upload.delay(report_id, 'pivot', result['items'])
            return string_status(self.request.task, insert_id)

        task_notification.delay(report_id=report_id, msg="This report is empty", status='warning')

    if check_status(context):
        notification_id = task_notification.delay(report_id=report_id, msg=context.text, status='error')
        return string_status(self.request.task, notification_id)
