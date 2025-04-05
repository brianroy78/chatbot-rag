from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import orm

Base = orm.declarative_base()


class Message(Base):
    __tablename__ = "message"
    id = sa.Column(sa.Integer, primary_key=True)
    content = sa.Column(sa.String(512), nullable=False)
    role = sa.Column(sa.Enum(Roles) nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    type = sa.Column(sa.String(120), nullable=False)

    conversation_id = sa.Column(sa.Integer, sa.ForeignKey("conversation.id"))


class Conversation(Base):
    __tablename__ = 'conversation'
    id = sa.Column(sa.Integer, primary_key=True)

    messages = orm.relationship("Message")
