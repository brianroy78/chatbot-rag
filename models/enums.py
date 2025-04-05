import enum


class Roles(enum.Enum):
    user = enum.auto()
    assistant = enum.auto()
    system = enum.auto()
    developer = enum.auto()


class ContentTypes(enum.Enum):
    text = enum.auto()
    image = enum.auto()
    audio = enum.auto()
    video = enum.auto()
    document = enum.auto()
    tool = enum.auto()
