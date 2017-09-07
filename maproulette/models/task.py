"""The Task model."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
Base = declarative_base()


class Task(Base):
    """The Task model."""

    __tablename__ = 'task'

    # Database identifier
    id = Column(Integer, primary_key=True)
    # Challenge (parent) relation
    challenge_id = Column(Integer, ForeignKey('challenge.id'))
    # Related OSM feature's identifier(s), JOSM format
    # https://josm.openstreetmap.de/wiki/Help/Action/DownloadObject
    osm_id = Column(String)
    # The Challenge owner can assign their own identifier to
    # keep track of the feature across updates.
    assigned_id = Column(Integer)
    # Task level instruction
    instruction = Column(String)
    # Task geometry
    geometry = Column(Geometry())
