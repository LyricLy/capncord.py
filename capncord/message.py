from . import channel

from .user import User

import datetime


class Message:

    def __init__(self, channel, id_, author, content, created_at):
        self.id = id_
        self.content = content
        self.channel = channel
        self.author = author
        self.created_at = created_at

    @classmethod
    def from_data(cls, bot, data):
        return cls(channel.Channel(bot, data["channel"]), data["message_id"],
                   User(bot, data["author_id"]),
                   data["content"],
                   datetime.datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S.%f"))
