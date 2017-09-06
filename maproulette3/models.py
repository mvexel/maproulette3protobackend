"""MapRoulette models."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
Base = declarative_base()


class Challenge(Base):
    """The Challenge model."""

    __tablename__ = 'challenge'

    # Database identifier
    id = Column(Integer, primary_key=True)
    # The Challenge owner can assign their own identifier to
    # keep track of the feature across updates.
    assigned_id = Column(Integer)
    # Challenge Title
    title = Column(String)
    # Description
    description = Column(String)
    # Challenge level instruction
    instruction = Column(String)
    # Backref to tasks
    tasks = relationship("Task", backref='challenge')


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


class User(Base):
    """The Challenge model."""

    __tablename__ = 'user'

    # Database identifier
    id = Column(Integer, primary_key=True)
    # OSM user identifier
    osm_id = Column(Integer)
    # OSM user name
    osm_username = Column(String)


if __name__ == '__main__':
    """Recreate tables. Careful: this will drop everything."""

    input("""
Dropping and re-creating MapRoulette tables.
Press ENTER to proceed or CTRL-c to back out.

""")

    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    input("""Done. Proceeding to add fixture data.
Press ENTER to proceed or CTRL-c to back out.

""")

    from utils import load_fixtures
    load_fixtures()

    print("Done.")
