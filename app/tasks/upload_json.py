import time, uuid, os
from app import celery
from app.libs.dataFrame import DataFrame

from app.tasks.inserts.webhook import task_webhook
from app.tasks.notification import task_notification

def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


@celery.task(name="upload.api", bind=True)
def task_upload(self, report_id, name, result):
    id = str(uuid.uuid4())
    colname = '%s__%s_%s' % (report_id, name, id)

    qtd = int(os.environ.get("MAESTRO_INSERT_QTD", 500))
    webhook_id = []
    for piece in batch(result, qtd):
        tt = task_webhook.delay(colname, piece, report_id)
        webhook_id.append(str(tt))

    prefetch = DataFrame(result[:50], False).getHeaders()
    notification_id = task_notification.delay(report_id=report_id, msg=id, status='finished', more={'columns': prefetch})
    return {'name': self.request.task, 'colname': colname, 'notification_id': str(notification_id), 'webhook-id': webhook_id}
