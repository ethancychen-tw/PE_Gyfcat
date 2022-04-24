import os

# Environment variables
if os.path.exists("config.env"):
    for line in open("config.env", "r"):
        var = line.strip().split("=", 1)
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace('"', "")


class Config:
    APP_NAME = os.environ.get("APP_NAME")
    if os.environ.get("SECRET_KEY"):
        SECRET_KEY = os.environ.get("SECRET_KEY")
    else:
        SECRET_KEY = "SECRET_KEY_ENV_VAR_NOT_SET"
        print("SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION")
    GFYCAT_CLIENT_ID = os.environ.get("GIFYCAT_CLIENT_ID")
    GFYCAT_CLIENT_SECRET = os.environ.get("GIFYCAT_CLIENT_SECRET")

    LINEBOT_MSG_CHANNEL_ACCESS_TOKEN = os.environ.get(
        "LINEBOT_MSG_CHANNEL_ACCESS_TOKEN", None
    )
    LINEBOT_MSG_CHANNEL_SECRET = os.environ.get("LINEBOT_MSG_CHANNEL_SECRET", None)

    ETHAN_LINE_USER_ID = os.environ.get("ETHAN_LINE_USER_ID", None)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    if not os.environ.get("SECRET_KEY"):
        raise Exception("SECRET_KEY IS NOT SET!")


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
