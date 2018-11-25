from .channel import OnlyChannel

from collections import defaultdict

import aiohttp


class Bot:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(headers={"User-Agent": "capn.py"}, loop=self.loop)
        self.listeners = {"message": [self.on_message]}
        self.lengths = defaultdict(int)

    async def on_message(self, message):
        pass

    async def check_for_messages(self):
        while True:
            for channel in self.get_all_channels():
                x = await channel.history()
                if len(x) != self.lengths[channel]:
                    await self.trigger_event("message", x[-1])
                self.lengths[channel] = len(x)
            await asyncio.sleep(1)

    def get_all_channels(self):
        return [OnlyChannel()]

    async def trigger_event(self, event, *args):
        for listener in self.listeners[event]:
            await listener(*args)

    def run():
        self.loop.create_task(on_ready())
        self.loop.create_task(check_for_messages())
        self.loop.run_forever()
