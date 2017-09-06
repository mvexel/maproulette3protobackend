"""The MapRoulette application entrypoint."""

from flask import Flask
from flask_restful import Api
from maproulette3.resources.task import Task
from maproulette3.resources.challenge import Challenge


app = Flask(__name__)


@app.route('/')
def index():
    """Show something for the site root."""
    return 'MapRoulette API -- nothing else to see here.'

api = Api(app)

api.add_resource(Task, '/task', '/task/<string:id>')
api.add_resource(Challenge, '/challenge', '/challenge/<string:id>')

if __name__ == "__main__":
    app.run()
