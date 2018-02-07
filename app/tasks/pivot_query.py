
import os
from app import celery
from .upload_json import task_upload
from app.libs.factoryOwnerRule import getRules


@celery.task(name="qpivot.api", bind=True)
def task_qpivot(self, owner_user, report_id, pipeline={}):
    print(owner_user, report_id, pipeline)
    return pipeline
    timeout = int(os.environ.get("MAESTRO_TIMEOUT_DISCOVERY", 10))

    path = FactoryURL.make("aggregation")
    rules = getRules(owner_user)

    jrules = json.dumps(rules)
    jpipeline = json.dumps(pipeline)

    context = requests.post(path, json={'owner': jrules, 'pipeline': jpipeline}, timeout=timeout)

    if context.status_code is 200:
        pass
    #return {'name': self.request.task, 'insert-id': insert_id}