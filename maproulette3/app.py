"""The MapRoulette application entrypoint."""

from flask import Flask
from flask_restful import Api
from maproulette3.resources.task import TaskResource
from maproulette3.resources.challenge import ChallengeResource

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

if __name__ == "__main__":
    app.run()
