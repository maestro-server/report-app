
import json
from pydash import has
from app import celery
from .upload_json import task_upload
from app.libs.factoryOwnerRule import getRules
from app.tasks.notification import task_notification
from app.repository.externalMaestroData import ExternalMaestroData


@celery.task(name="qgeneral.api")
def task_qgeneral(owner_user, report_id, type, filters={}):
    type = type.lower()
    rules = getRules(owner_user)
    query = {**rules, **filters}
    fjson = json.dumps(query)

    result = ExternalMaestroData(entity_id=report_id) \
        .post_request(path=type, body={'query': fjson, 'limit': 99999}) \
        .get_results()

    if has(result, 'found') and result['found'] > 0:
        insert_id = task_upload.delay(report_id, owner_user, 'general', result['items'])

        return {'upload-id': insert_id}

    task_notification.delay(report_id=report_id, msg="This report is empty", status='warning')