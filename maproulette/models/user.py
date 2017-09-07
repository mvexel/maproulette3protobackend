"""The User model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class User(Base):
    """The User model."""

    __tablename__ = 'user'

    # Database identifier
    id = Column(Integer, primary_key=True)
    # OSM user identifier
    osm_id = Column(Integer)
    # OSM user name
    osm_username = Column(String)
    # Challenges this user has
    challenges = relationship("Challenge", backref='owner_id')
