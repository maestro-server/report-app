
from app.views import app
from app import celery
from app.repository.externalMaestro import ExternalMaestro
from app.services.privateAuth.decorators.external_private_token import create_jwt


@celery.task(name="notification.api")
def task_notification(report_id, msg="completed", status='success', more={}):
    data = {'_id': report_id, 'status': status, 'msg': msg}
    merged = {**data, **more}

    base = app.config['MAESTRO_DATA_URI']

    ExternalMaestro(base) \
    .set_headers(create_jwt()) \
    .put_request(path="reports", body={'body': [merged]})

    return {'conn_id': report_id, 'status': merged.get('status'), 'id': merged.get('_id ')}
