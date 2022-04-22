import os

# Environment variables
if os.path.exists("config.env"):
    for line in open("config.env", "r"):
        var = line.strip().split("=")
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace('"', "")


class Config:
    APP_NAME = os.environ.get("APP_NAME")
    GFYCAT_CLIENT_ID = os.environ.get("GIFYCAT_CLIENT_ID")
    GFYCAT_CLIENT_SECRET = os.environ.get("GIFYCAT_CLIENT_SECRET")

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
