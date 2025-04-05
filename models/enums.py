import enum


class Roles(enum.Enum):
    user = enum.auto()
    assistant = enum.auto()
    system = enum.auto()
    developer = enum.auto()
