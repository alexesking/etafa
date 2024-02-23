import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID",26984209))

    API_HASH = os.environ.get("API_HASH", "41fd74787472ed074ad7a0c117df2530")
