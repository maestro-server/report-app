
from app import celery


@celery.task(name="uplaod.api", bind=True)
def task_upload(self, date):

    return {'name': self.request.task}