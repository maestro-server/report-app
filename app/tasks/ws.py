
from app import celery
from app.repository.externalMaestroWS import ExternalMaestroWS

@celery.task(name="ws.api")
def task_ws(colname, owner_id, status='success'):
    msg = "Finish Sync"
    channel = "maestro#%s" % owner_id

    print(msg, channel)

    body = {
        "method": "publish",
        "params": {
            "channel": channel,
            "data": {
                "notify": {
                    "title": colname,
                    "msg": msg,
                    "type": status
                },
                "event": {
                    "caller": "connections-update"
                }
            }
        }
    }

    result = ExternalMaestroWS()\
        .auth_header()\
        .post_request(path="api", body=body)\
        .get_results()

    return {'result': result, 'task': 'ws-notification'}