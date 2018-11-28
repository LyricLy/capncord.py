from .http import post


class User:
    def __init__(self, bot, id):
        self.bot = bot
        self.id = id
        self._name = None
        self._messages_sent = None

    async def update(self):
        if not (self._name is None or self._messages_sent is None):
            return
        resp = await post(self.bot.session, "/get_user", data={"id": self.id})
        data = await resp.json()
        self._name = data["name"]
        self._messages_sent = data["messages_sent"]

    @property
    async def name(self):
        await self.update()
        return self._name

    @property
    async def messages_sent(self):
        await self.update()
        return self._messages_sent

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.id == other.id

    def __str__(self):
        if self._name:
            return self._name
        return repr(self)
