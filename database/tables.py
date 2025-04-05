from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    message = Column(String(512), unique=True, nullable=False)
    role = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    type = Column(String(120), nullable=False)
