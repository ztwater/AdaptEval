# async_wrap_iter definition as above

import time

def test_iter():
    for i in range(5):
        yield i
        time.sleep(1)

async def test():
    ait = async_wrap_iter(test_iter())
    async for i in ait:
        print(i)

async def heartbeat():
    while True:
        print('alive')
        await asyncio.sleep(.1)

async def main():
    asyncio.create_task(heartbeat())
    await test()

asyncio.run(main())
