import os
from flask import Flask
from app.config import config
from app.integrations.gifycat import GfycatCaller

gfycat_caller = GfycatCaller(
    client_id=config[os.environ.get("FLASK_ENV")].GFYCAT_CLIENT_ID,
    client_secret=config[os.environ.get("FLASK_ENV")].GFYCAT_CLIENT_SECRET,
)


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    return app
