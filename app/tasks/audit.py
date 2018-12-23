
from app import celery
from app.repository.externalMaestroAudit import ExternalMaestroAudit

@celery.task(name="audit.api")
def task_audit(entity_id, tmp):

    path = "audit/reports/%s" % entity_id

    try:
        results = ExternalMaestroAudit()\
                    .put_request(path=path, body=tmp)\
                    .get_results()

        return {'api': results}

    except Exception as error:
        return {'message': str(error)}