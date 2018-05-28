
import os, json, requests
from app import celery
from app.libs.url import FactoryURL
from .upload_json import task_upload
from .notification import task_notification


@celery.task(name="qpivot.api", bind=True)
def task_qpivot(self, owner_user, report_id, entity, pipeline={}):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_DATA", 10))

    path = FactoryURL.make("aggregate", resource="MAESTRO_URL")
    jpipeline = json.dumps(pipeline)

    context = requests.post(path, json={'entity': entity, 'pipeline': jpipeline}, timeout=timeout)

    if context.status_code is 200:
        result = context.json()
        if result['items']:
            insert_id = task_upload.delay(report_id, 'pivot', result['items'])
            return {'name': self.request.task, 'upload-id': str(insert_id)}

        task_notification.delay(report_id=report_id, msg="This report is empty", status='warning')

    if context.status_code in [400, 403, 404, 500, 501, 502, 503]:
        notification_id = task_notification.delay(report_id=report_id, msg=context.text, status='error')
        return {'name': self.request.task, 'notification-id': str(notification_id)}