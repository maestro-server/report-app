
import requests, datetime
from app import celery
from app.libs.url import FactoryURL

@celery.task(name="notification.api", bind=True)
def task_notification(self, report_id, msg, status='success'):
    data = {'_id': report_id, 'status': status, 'msg': msg}

    path = FactoryURL.make(path="reports")
    ret = requests.put(path, json={'body': [data]})

    return {'name': self.request.task, 'report_id': report_id, 'status': status}