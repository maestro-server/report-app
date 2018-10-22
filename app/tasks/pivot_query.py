
from app import celery
from .upload_json import task_upload
from .notification import task_notification
from app.repository.externalMaestroData import ExternalMaestroData


@celery.task(name="qpivot.api")
def task_qpivot(owner_user, report_id, entity, pipeline=[]):

    result = ExternalMaestroData(report_id) \
        .list_aggregation(path="aggregate", entity=entity, pipeline=pipeline) \
        .get_results('items')

    if result:
        insert_id = task_upload.delay(report_id, owner_user, 'pivot', result)
        return {'insert-id': str(insert_id)}

    task_notification.delay(report_id=report_id, msg="This report is empty", status='warning')
