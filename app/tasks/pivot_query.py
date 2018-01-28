
import os
from app import celery
from .upload_json import task_upload


@celery.task(name="qgeneral.api", bind=True)
def task_qgeneral(self, type, filters):
    insert_id = task_upload.delay()

    return {'name': self.request.task, 'insert-id': insert_id}