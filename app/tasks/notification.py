
from app.views import app
from app import celery
from app.repository.externalMaestro import ExternalMaestro


@celery.task(name="notification.api")
def task_notification(report_id, msg, status='success', more={}):
    data = {'_id': report_id, 'status': status, 'msg': msg}
    merged = {**data, **more}

    base = app.config['MAESTRO_DATA_URI']
    ExternalMaestro(base) \
        .put_request(path="reports", body={'body': [merged]})

    return {'conn_id': report_id}