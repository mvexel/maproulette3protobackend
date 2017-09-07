"""Defines the Task resource."""

from flask_restful import Resource, abort, fields, marshal_with
from maproulette.models import Task
from maproulette.db import session
from maproulette.utils import GeoJSONField

task_fields = {
    'id': fields.Integer,
    'challenge_id': fields.Integer,
    'osm_id': fields.Integer,
    'assigned_id': fields.Integer,
    'instruction': fields.String,
    'geometry': GeoJSONField()
}


class TaskResource(Resource):
    """The Task Resource."""

    @marshal_with(task_fields)
    def get(self, id):
        """HTTP GET."""
        task = session.query(Task).filter(Task.id == id).first()
        if not task:
            abort(404, message="Task {} doesn't exist".format(id))
        return task

    def put(self):
        """HTTP PUT."""
        pass

    def post(self):
        """HTTP POST."""
        pass

    def delete(self):
        """HTTP DELETE."""
        pass
