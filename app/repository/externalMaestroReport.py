
from app.views import app
from app.libs.logger import logger
from .externalMaestro import ExternalMaestro
from app.repository.libs.notifyError import notify_error

class ExternalMaestroReport(ExternalMaestro):
    
    def __init__(self, entity_id=None):
        base = app.config['MAESTRO_REPORT_URI']
        self.ent_id = entity_id

        super().__init__(base)

    def error_handling(self, task, msg):

        if self.ent_id :
            return notify_error(task=task, msg=msg, conn_id=self.ent_id)

        logger.error("MaestroData:  [%s] - %s", task, msg)