
from app import celery
from app.repository.reports import Reports
from app.repository.externalMaestroReport import ExternalMaestroReport


@celery.task(name="webhook.api")
def task_webhook(colname, results, report_id):

    result = ExternalMaestroReport(entity_id=report_id) \
        .post_request(path="reports", body={'colname': colname, 'results': results}) \
        .get_results()

    return {'qtd': len(results)}