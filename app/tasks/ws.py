
from app import celery
from app.repository.externalMaestroWS import ExternalMaestroWS

@celery.task(name="ws.api")
def task_ws(name, report_id, owner_id, status='success'):
    msg = "Finish Sync"
    title = "%s (%s)" % (name, report_id)
    channel = "maestro-%s" % owner_id

    body = {
        "method": "publish",
        "params": {
            "channel": channel,
            "data": {
                "notify": {
                    "title": title,
                    "msg": msg,
                    "type": status
                },
                "event": {
                    "caller": ["reports-update", "reports-{}".format(report_id)]
                }
            }
        }
    }

    result = ExternalMaestroWS()\
        .auth_header()\
        .post_request(path="api", body=body)\
        .get_results()

    return {'result': result, 'task': 'ws-notification'}