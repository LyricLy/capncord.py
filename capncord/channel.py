from . import message

from .http import get, post
from .user import User


class Channel:
    def __init__(self, bot, id):
        self.bot = bot
        self.id = id

    async def send(self, content):
        await post(self.bot.session, "/chat", data={"text": content, "channel": self.id})

    async def history(self):
        resp = await get(self.bot.session, "/serial_chat")
        data = await resp.json()
        return [message.Message.from_data(bot, msg) for msg in data if msg["channel"] == self.id]

    def __hash__(self):
        return 0
