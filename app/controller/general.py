import json
from flask_restful import Resource

from app.libs.logger import logger
from app.services.factoryFilter import FactoryFilters
from app.validate.generalValidate import Validate
from app.tasks.general_query import task_qgeneral
from app.tasks.notification import task_notification


class GeneralReport(Resource):
    """
    @api {post} /reports/general/ Create general graph
    @apiName PostGeneral
    @apiGroup Reports

    @apiParam(Param) {String} report_id Report ID, created by server app
    @apiParam(Param) {String} component Main Component [servers, applications, volumes, network, systems, clients, datacenters]
    @apiParam(Param) {String} owner_user User/Team Id [uuid]
    @apiParam(Param) {Json} filters List of filters.
    <br/>
    <pre class="prettyprint language-json" data-type="json">
    <code>[{
    <br/>    field: "(String)",
    <br/>    filter: "(String value)",
    <br/>    comparer: "(Equal type)", //equal, contain, not contain
    <br/>    typ: "(Field Type)" //boolean, string, date
    <br/>}]
    </code>
    </pre>
    <br/>
    <pre class="prettyprint language-json" data-type="json">
    <code>[{
    <br/>    field: "active",
    <br/>    filter: "true",
    <br/>    comparer: "equal",
    <br/>    typ: "boolean"
    <br/>}]
    </code>
    </pre>

    @apiError (Error) BadRequest Missing parameters
    @apiError (Error) NotFound List is empty

    @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
                {
                'filter': {List of filters},
                'general-id': (Report ID)
                }
    """
    
    def post(self):
        valid = Validate().validate()

        if valid:
            prepared = None
            try:
                filters = json.loads(valid['filters'])
                prepared = FactoryFilters.factory(input=filters)
            except Exception as error:
                task_notification.delay(report_id=valid['report_id'], msg=str(error), status='error')
                logger.error("Report: Task [general] - %s", error)
                return {'message': str(error)}, 501

            if (prepared is not None):
                general_id = task_qgeneral.delay(valid['owner_user'], valid['report_id'], valid['component'], prepared)

                return {'filter': valid['filters'], 'general-id': str(general_id)}

        return valid, 502
