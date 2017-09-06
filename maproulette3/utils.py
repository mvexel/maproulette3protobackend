"""MapRoulette Utility functions."""


def load_fixtures():
    """Load some fixture data into the database."""
    from models import Task, Challenge, User
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from settings import DB_URI
    from random import randrange, random

    # Set up the SQLAlchemy session
    engine = create_engine(DB_URI)
    session = sessionmaker(bind=engine)
    s = session()

    # Create a user
    u = User()
    u.osm_id = 8909
    u.osm_username = 'mvexel'
    s.add(u)

    for x in range(1, 11):
        c = Challenge()
        c.name = "Challenge {}".format(x)
        c.instruction = "Challenge {} Instruction".format(x)
        s.add(c)

    for x in range(1, 10000):
        t = Task()
        t.challenge_id = randrange(1, 11)
        t.geometry = 'POINT({lon} {lat})'.format(
            lon=random() * 360 - 180,
            lat=random() * 180 - 90)
        s.add(t)

    s.commit()
    s.close()
