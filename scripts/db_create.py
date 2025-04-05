from sqlalchemy import create_engine

from database.tables import Base
from settings import Settings

Base.metadata.create_all(create_engine(Settings.DB_URL))
