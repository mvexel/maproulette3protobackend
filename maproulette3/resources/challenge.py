"""Defines the Challenge resource."""

from flask_restful import Resource, abort, fields, marshal_with
from models import Challenge
from db import session

challenge_fields = {
    'id': fields.Integer,
    'assigned_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'instruction': fields.String,
}


class ChallengeResource(Resource):
    """The Challenge Resource."""

    @marshal_with(challenge_fields)
    def get(self, id):
        """HTTP GET."""
        challenge = session.query(Challenge).filter(Challenge.id == id).first()
        if not challenge:
            abort(404, message="Task {} doesn't exist".format(id))
        return challenge

    def put(self):
        """HTTP PUT."""
        pass

    def post(self):
        """HTTP POST."""
        pass

    def delete(self):
        """HTTP DELETE."""
        pass
