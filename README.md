# capncord.py

capncord.py is an API wrapper for Discord written in Python.

## Installing

To install the library, run the following command:

```
pip install capncord.py
```

Depending on your environment, the command may be slightly different. If you're having trouble installing the library, familiarize yourself with how `pip` works on your platform first.

## Tutorial

To create a bot, subclass `capncord.Bot` and overload `on_ready` and `on_message`.

### Bot

The Bot class supports the methods `async def wait_for(event: str, check: Optional[function] = None, timeout: Optional[int] = None`, `async def get_message(id: int) -> Message`, `async def history() -> List[Message]` and `async def get_channel(id: int) -> Channel`.

`history()` returns a list of messages sent in all channels with the most recent messages at the start of the list.

It also has the attributes `loop: asyncio.BaseEventLoop`, `session: aiohttp.ClientSession` and `user: User`.

### Message

The Message class has the attributes `id: int`, `created_at: datetime.datetime`, `content: str`, `author: User` and `channel: Channel`.

### Channel

The Channel class supports the methods `async def send(content: str)` and `async def history() -> List[Message]`.

`history()` returns a list of messages sent in this channel with the most recent messages at the start of the list.

It also has the attribute `id`.

### User

The User class supports `str`.

It also has the attributes `await User.name` and `await User.messages_sent`.

## Requirements

* Python 3.5.3+
* ``aiohttp`` library
* ``websockets`` library

Usually ``pip`` will handle these for you.
