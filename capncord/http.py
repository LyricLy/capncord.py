import asyncio

from contextlib import contextmanager


BASE_URL = "https://capnchat.tk"

def route(n):
    return BASE_URL + n

async def get(session, route_):
    resp = await session.get(route(route_))
    if resp.status == 429:
        await asyncio.sleep(1)
        await get(session, route_)
    return resp

async def post(session, route_, *, data=None):
    resp = await session.post(route(route_), data=data)
    if resp.status == 429:
        await asyncio.sleep(1)
        await post(session, route_, data=data)
    return resp
