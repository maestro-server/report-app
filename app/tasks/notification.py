
import requests
from app import celery
from app.libs.url import FactoryDataURL

@celery.task(name="notification.api", bind=True)
def task_notification(self, report_id, msg, status='success', more={}):
    data = {'_id': report_id, 'status': status, 'msg': msg}
    merged = {**data, **more}

    path = FactoryDataURL.make(path="reports")
    ret = requests.put(path, json={'body': [merged]})

    return {'name': self.request.task, 'report_id': report_id, 'status': status}