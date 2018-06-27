import requests
import os
from app import celery
from app.libs.url import FactoryReportURL
from app.libs.statusCode import check_status
from app.libs.notifyError import notify_error


@celery.task(name="webhook.api", bind=True)
def task_webhook(self, name, result, report_id):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_WEBHOOK", 5))

    try:
        path = FactoryReportURL.make(path="reports")
        context = requests.post(path, json={'colname': name, 'results': result}, timeout=timeout)
    except Exception as error:
        notify_error(self.request.task, report_id, str(error))
        return str(error), 500

    if check_status(context):
        return notify_error(self.request.task, report_id, context.text)

    return {'name': self.request.task, 'status_code': context.status_code, 'qtd': len(result)}