
import os
from app import celery
from .upload_json import task_upload


@celery.task(name="qpivot.api", bind=True)
def task_qpivot(self, owner_user, report_id, filters={}):
    print(owner_user, report_id, filters)
    

    #return {'name': self.request.task, 'insert-id': insert_id}