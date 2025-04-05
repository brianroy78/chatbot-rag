from typing import Optional

from sqlalchemy.future import Engine
from sqlalchemy.orm import Session, sessionmaker


class Data:
    URL: str
    ENGINE: Optional[Engine]
    SESSION_MAKER: Optional[sessionmaker]


def get_session() -> Session:
    assert Data.SESSION_MAKER is not None
    return Data.SESSION_MAKER()
