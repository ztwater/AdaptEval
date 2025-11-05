import asyncio, threading

def async_wrap_iter(var_0):
    """Wrap blocking iterator into an asynchronous one"""
    var_1 = asyncio.get_event_loop()
    var_2 = asyncio.Queue(1)
    var_3 = None
    var_4 = object()

    async def yield_queue_items():
        while True:
            var_5 = await var_2.get()
            if var_5 is var_4:
                break
            yield var_5
        if var_3 is not None:
            # the iterator has raised, propagate the exception
            raise var_3

    def iter_to_queue():
        nonlocal var_3
        try:
            for item in var_0:
                # This runs outside the event loop thread, so we
                # must use thread-safe API to talk to the queue.
                asyncio.run_coroutine_threadsafe(q.put(item), loop).result()
        except Exception as e:
            var_3 = e
        finally:
            asyncio.run_coroutine_threadsafe(q.put(_END), loop).result()

    threading.Thread(target=iter_to_queue).start()
    return yield_queue_items()
