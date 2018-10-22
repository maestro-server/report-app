
from app import celery
from app.repository.externalMaestroReport import ExternalMaestroReport


@celery.task(name="webhook.api")
def task_webhook(name, result, report_id):

    result = ExternalMaestroReport(entity_id=report_id) \
        .post_request(path="reports", body={'colname': name, 'results': result}) \
        .get_results()

    return {'result': result, 'qtd': len(result)}