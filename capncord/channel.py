from . import message

from .http import get, post
from .user import User


class Channel:

    def __init__(self, bot, id_):
        self.bot = bot
        self.id = id_

    async def send(self, content):
        await post(self.bot.session, "/chat", data={"text": content, "channel": self.id})

    async def history(self):
        resp = await get(self.bot.session, "/serial_chat")
        data = await resp.json()
        return [message.Message.from_data(self.bot, msg) for msg in data if msg["channel"] == self.id]

    def __eq__(self, other):
        if not isinstance(other, Channel):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return self.id
