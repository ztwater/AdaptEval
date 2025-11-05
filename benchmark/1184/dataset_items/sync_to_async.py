from concurrent.futures import ThreadPoolExecutor
from typing import AsyncGenerator, Iterable, Optional
import asyncio


def async_wrap_iter(it: Iterable, pool: Optional[ThreadPoolExecutor] = None) -> AsyncGenerator:
    loop = asyncio.get_event_loop()
    q = asyncio.Queue(1)
    exception = None
    _END = object()

    async def yield_queue_items():
        while True:
            next_item = await q.get()
            if next_item is _END:
                break
            yield next_item
        if exception is not None:
            # the iterator has raised, propagate the exception
            raise exception

    def iter_to_queue():
        nonlocal exception
        try:
            for item in it:
                asyncio.run_coroutine_threadsafe(q.put(item), loop).result()
        except Exception as e: 
            exception = e
        finally:
            asyncio.run_coroutine_threadsafe(q.put(_END), loop).result()

    loop.run_in_executor(pool, iter_to_queue)
    return yield_queue_items()
