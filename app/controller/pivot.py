import json
from flask_restful import Resource
from app.repository.model import Model
from app.services.privateAuth import private_auth
from app.validate.pivotValidate import Validate
from app.services.pivotPipeline import PivotPipeline
from app.tasks.pivot_query import task_qpivot
from app.tasks.notification import task_notification


class PivotReport(Resource):
    """
    @api {patch} /reports/pivot Update pivot graph
    @apiName UpdatePivot
    @apiGroup Reports
    @apiDescription Same contract of post
    """

    @private_auth
    def patch(self):
        return self.post()

    @private_auth
    def post(self):
        """
        @api {post} /reports/pivot Create a pivot graph
        @apiName PostPivot
        @apiGroup Reports

        @apiParam(Param) {String} report_id Report ID, created by server app
        @apiParam(Param) {String} owner_user User/Team Id [uuid]
        @apiParam(Param) {Json} filters List of filters.
        <br/>
        <pre class="prettyprint language-json" data-type="json">
        <code>filters: {
        <br/>    applications: {
        <br/>        enabled: true
        <br/>        filters: [{
        <br/>            field: "(String)",
        <br/>            filter: "(String value)",
        <br/>            comparer: "(Equal type)", //equal, contain, not contain
        <br/>            typ: "(Field Type)" //boolean, string, date
        <br/>        }]
        <br/>        icon: "fa-code"
        <br/>        title: "Applications"
        <br/>    }
        <br/>    clients: {title: "Clients", icon: "fa-user-o", enabled: true,…}
        <br/>    servers: {title: "Servers", icon: "fa-server", enabled: true,…}
        <br/>    systems: {title: "Systems", icon: "fa-briefcase", enabled: true,…}
        <br/>}
        </code>
        </pre>

        @apiSuccessExample {json} Success-Response:
                HTTP/1.1 201 OK
                 {
                    pivot-id: <entry task id>,
                    name: "pivot - (date time)",
                    report: "pivot"
                    status: "(String)",
                    filters: {clients: {title: "Clients", icon: "fa-user-o", enabled: true,…},…}
                }
        """
        PPipeline = PivotPipeline()
        valid = Validate().validate()

        if valid:
            try:
                filters = json.loads(valid['filters'])
                PPipeline.factory(input=filters, owner_id=valid['owner_user'])
            except Exception as error:
                task_notification.delay(report_id=valid['report_id'], msg=str(error), status='error')
                return {'message': str(error)}, 501

            if PPipeline.hasResult():
                colname = '%s_%s' % (valid['report_id'], 'pivot')
                data = Model().deleteCollection(colname)

                pivot_id = task_qpivot.delay(valid['owner_user'], valid['report_id'], PPipeline.getFirst(),
                                             PPipeline.getResult())

                return {'filter': valid['filters'], 'pivot-id': str(pivot_id)}

        return valid, 502