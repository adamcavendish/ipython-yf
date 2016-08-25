import asyncio
import time
from yf_debug import yf_debug

@asyncio.coroutine
def test():
    print('in test')
    time.sleep(2)
    print('out test')
    t = {'1': 2}
    return t

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

yf_debug(test)
yf_debug(print_sum, 1, 2)

