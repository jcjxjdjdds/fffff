import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 25901632))

    API_HASH = os.environ.get("API_HASH", "caac15797ce3785ae427cda6318b85c9")
