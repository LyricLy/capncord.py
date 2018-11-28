from .abc import Messageable
from .channel import OnlyChannel
from .http import get
from .user import User
from .message import Message

import asyncio
import json

from collections import defaultdict

import aiohttp
import websockets


class Bot(Messageable):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.session = None
        self.user = None
        self.listeners = {"message": [self.on_message], "ready": [self.on_ready]}
        self.lengths = defaultdict(int)

    async def send(self, *args, **kwargs):
        await OnlyChannel(self).send(*args, **kwargs)

    async def history(self, *args, **kwargs):
        return await OnlyChannel(self).history(*args, **kwargs)

    async def get_message(self, *args, **kwargs):
        return await OnlyChannel(self).get_message(*args, **kwargs)

    async def on_message(self, message):
        pass

    async def on_ready(self):
        pass

    async def wait_for(self, event, *, timeout=None, check=None):
        fut = asyncio.Future()
        async def listener(*args):
            if check and check(*args):
                if len(args) == 1:
                    fut.set_result(args[0])
                else:
                    fut.set_result(args)
        self.listeners[event].append(listener)
        return await asyncio.wait_for(fut, timeout=timeout)

    async def check_for_messages(self):
        while not hasattr(self, "ws"):
            await asyncio.sleep(0)
        while True:
            msg = json.loads(await self.ws.recv())
            await self.trigger_event("message", Message.from_data(msg, OnlyChannel(self)))

    def get_all_channels(self):
        return [OnlyChannel(self)]

    async def trigger_event(self, event, *args):
        for listener in self.listeners[event]:
            self.loop.create_task(listener(*args))

    async def prep(self, token):
        self.ws = await websockets.client.connect("ws://capnchat.tk:8000/ws")
        self.session = aiohttp.ClientSession(headers={"User-Agent": "capn.py", "token": token}, loop=self.loop)
        resp = await get(self.session, "/id")
        data = await resp.json()
        self.user = User(self, data["user_id"])
        await self.trigger_event("ready")

    def run(self, token):
        self.loop.create_task(self.check_for_messages())
        self.loop.create_task(self.prep(token))
        self.loop.run_forever()
        self.session.close()
