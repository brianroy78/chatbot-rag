import configparser

config = configparser.ConfigParser()
config.read('./alembic.ini')

DB_URL = config["alembic"]["sqlalchemy.url"]
