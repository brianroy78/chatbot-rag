import configparser

config = configparser.ConfigParser()
config.read('./alembic.ini')


class Settings:
    DB_URL = config["alembic"]["sqlalchemy.url"]
