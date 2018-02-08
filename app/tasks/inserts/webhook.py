import requests, os
from app import celery
from app.libs.url import FactoryURL


@celery.task(name="webhook.api", bind=True)
def task_webhook(self, name, result):
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_WEBHOOK", 5))

    path = FactoryURL.make(path="reports", resource="MAESTRO_URL")
    context = requests.post(path, json={'colname': name, 'results': result}, timeout=timeout)
    return {'name': self.request.task, 'status_code': context.status_code, 'qtd': len(result), 'result': context.json()}