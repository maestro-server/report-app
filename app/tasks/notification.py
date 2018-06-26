import requests
from app import celery
from app.libs.logger import logger
from app.libs.url import FactoryDataURL
from app.libs.statusCode import check_status


@celery.task(name="notification.api", bind=True)
def task_notification(self, report_id, msg, status='success', more={}):
    data = {'_id': report_id, 'status': status, 'msg': msg}
    merged = {**data, **more}

    path = FactoryDataURL.make(path="reports")
    context = requests.put(path, json={'body': [merged]})

    if check_status(context):
        logger.error("Reports: TASK [notification] - %s", context.text)

    return {'name': self.request.task, 'report_id': report_id, 'status': context.status_code}
