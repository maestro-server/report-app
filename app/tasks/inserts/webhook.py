
import requests, os
from app import celery
from app.libs.url import FactoryReportURL
from app.tasks.notification import task_notification

@celery.task(name="webhook.api", bind=True)
def task_webhook(self, name, result, report_id):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_WEBHOOK", 5))

    path = FactoryReportURL.make(path="reports")
    context = requests.post(path, json={'colname': name, 'results': result}, timeout=timeout)

    if context.status_code in [400, 403, 404, 500, 501, 502, 503]:
         notification_id = task_notification.delay(report_id=report_id, msg=context.text, status='error')
         return {'name': self.request.task, 'notification-id': str(notification_id)}
    
    return {'name': self.request.task, 'status_code': context.status_code, 'qtd': len(result)}