import asyncio
from asyncio import wait

async def hello():
    print('hello')
    await asyncio.sleep(3)
    print('world')


loop = asyncio.get_event_loop()
coro = [hello(), hello(), hello()]
loop.run_until_complete(asyncio.ensure_future(coro))

