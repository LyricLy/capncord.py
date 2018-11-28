from .http import get, post
from .user import User
from .message import Message

from .abc import Messageable


class OnlyChannel(Messageable):
    async def send(self, content):
        await post(self.bot.session, "/chat", data={"text": content})

    async def history(self):
        resp = await get(self.bot.session, "/serial_chat")
        data = await resp.json()
        return [Message.from_data(msg, self) for msg in data]

    async def get_message(self, id):
        resp = await post(self.bot.session, "/get_message", data={"id": id})
        data = await resp.json()
        return Message.from_data(data, self)

    def __hash__(self):
        return 0
