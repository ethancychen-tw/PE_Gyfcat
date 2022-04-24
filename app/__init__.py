import os
from flask import Flask
from app.config import config
from app.integrations.gifycat import GfycatCaller
from linebot import LineBotApi, WebhookHandler

gfycat_caller = GfycatCaller(
    client_id=config[os.environ.get("FLASK_ENV")].GFYCAT_CLIENT_ID,
    client_secret=config[os.environ.get("FLASK_ENV")].GFYCAT_CLIENT_SECRET,
)


line_bot_api = LineBotApi(
    config[os.environ.get("FLASK_ENV")].LINEBOT_MSG_CHANNEL_ACCESS_TOKEN
)
handler = WebhookHandler(config[os.environ.get("FLASK_ENV")].LINEBOT_MSG_CHANNEL_SECRET)

from app.integrations.linebot import callback


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.add_url_rule(
        "/linebot_callback", "linebot_callback", callback, methods=["POST"]
    )

    return app
