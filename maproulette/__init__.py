"""The MapRoulette application entrypoint."""

from flask import Flask
from flask_restful import Api
from maproulette.resources.task import TaskResource
from maproulette.resources.challenge import ChallengeResource
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from maproulette.settings import DB_URI

app = Flask(__name__)


# Initialize application
@app.route('/')
def index():
    """Show something for the site root."""
    return 'MapRoulette API -- nothing else to see here.'

api = Api(app)

# Add resource endpoints
api.add_resource(TaskResource, '/task', '/task/<string:id>')
api.add_resource(ChallengeResource, '/challenge', '/challenge/<string:id>')

Base = declarative_base()
engine = create_engine(DB_URI)


@app.cli.command()
def initdb():
    """Initialize the application database."""
    Base.metadata.create_all(engine)


@app.cli.command()
def dropdb():
    """Drop the application database."""
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)


@app.cli.command()
def loadfixtures():
    """Load fixture data into application DB."""
    from maproulette.utils import load_fixtures
    load_fixtures()


if __name__ == "__main__":
    app.run()
