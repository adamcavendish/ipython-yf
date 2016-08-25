import asyncio

def yf_debug(f, *args, **kwargs):
    @asyncio.coroutine
    def debug_helper(f, *args, **kwargs):
        return (yield from f(*args, **kwargs))
    original_loop = asyncio.get_event_loop()
    loop = asyncio.SelectorEventLoop()
    asyncio.set_event_loop(loop)
    try:
        ans = loop.run_until_complete(debug_helper(f, *args, **kwargs))
    finally:
        loop.close()
    asyncio.set_event_loop(original_loop)
    return ans

__all__ = ["yf_debug"]

