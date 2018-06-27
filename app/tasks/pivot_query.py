import os
import json
import requests
from .upload_json import task_upload
from .notification import task_notification
from app import celery
from app.libs.url import FactoryDataURL
from app.libs.statusCode import check_status, string_status
from app.libs.notifyError import notify_error


@celery.task(name="qpivot.api", bind=True)
def task_qpivot(self, report_id, entity, pipeline={}):
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
        return notify_error(self.request.task, report_id, context.text)
