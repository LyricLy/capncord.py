from ._utils import route

from .abc import Messageable


class OnlyChannel(Messageable):
    async def send(self, content):
        async with self.bot.session.post(route("/chat"), params={"text": content}) as resp:
            return Message(content, self)

    async def history(self):
        async with self.bot.session.get(route("/serial_chat")) as resp:
            data = await resp.json()
            return list(map(Message, data))

    def __hash__(self):
        return 0
