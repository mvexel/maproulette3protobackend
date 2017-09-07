"""MapRoulette Utility functions."""

from flask_restful import fields
import json
from maproulette.db import session
from geoalchemy2 import functions


class GeoJSONField(fields.Raw):
    """GeoJSON output definition for geometry field."""

    def format(self, value):
        """Reformat WKT input as GeoJSON."""
        return json.loads(
            session.scalar(
                functions.ST_AsGeoJSON(value)))


def load_fixtures():
    """Load some fixture data into the database."""
    from maproulette.models import Task, Challenge, User
    from random import randrange, random

    # Create a user
    u = User()
    u.osm_id = 8909
    u.osm_username = 'mvexel'
    session.add(u)

    for x in range(1, 11):
        c = Challenge()
        c.name = "Challenge {}".format(x)
        c.instruction = "Challenge {} Instruction".format(x)
        session.add(c)

    for x in range(1, 10000):
        t = Task()
        t.challenge_id = randrange(1, 11)
        t.geometry = 'POINT({lon} {lat})'.format(
            lon=random() * 360 - 180,
            lat=random() * 180 - 90)
        session.add(t)

    session.commit()
