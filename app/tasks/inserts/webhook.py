import requests
import os
from app import celery
from app.libs.url import FactoryReportURL
import app.libs.statusCode


@celery.task(name="webhook.api", bind=True)
def task_webhook(self, name, result, report_id):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_WEBHOOK", 5))

    path = FactoryReportURL.make(path="reports")
    context = requests.post(path, json={'colname': name, 'results': result}, timeout=timeout)

    if check_status(context):
        return notify_error(self.request.tas, report_id, context.text)

    return {'name': self.request.task, 'status_code': context.status_code, 'qtd': len(result)}
