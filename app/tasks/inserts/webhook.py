import requests
import os
from app import celery
from app.libs.url import FactoryReportURL
from app.tasks.notification import task_notification
from app.libs.status_code import check_status, string_status


@celery.task(name="webhook.api", bind=True)
def task_webhook(self, name, result, report_id):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_WEBHOOK", 5))

    path = FactoryReportURL.make(path="reports")
    context = requests.post(path, json={'colname': name, 'results': result}, timeout=timeout)

    if check_status(context):
        notification_id = task_notification.delay(report_id=report_id, msg=context.text, status='error')
        return string_status(self.request.task, notification_id)

    return {'name': self.request.task, 'status_code': context.status_code, 'qtd': len(result)}
