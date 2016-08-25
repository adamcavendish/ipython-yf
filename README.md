# iPython-yf

### An iPython Extension inspired by [tecki/ipython-yf](https://github.com/tecki/ipython-yf)

---

## Install

Put `yf.py` to anywhere ipython can load

```
In [1]: %load_ext yf

In [2]: import asyncio

In [3]: async def compute(x, y):
   ...:         print("Compute %s + %s ..." % (x, y))
   ...:         await asyncio.sleep(1.0)
   ...:         return x + y
   ...: 

In [4]: async def print_sum(x, y):
   ...:         result = await compute(x, y)
   ...:         print("%s + %s = %s" % (x, y, result))
   ...:     

In [5]: yield from print_sum(1,2)
Compute 1 + 2 ...
1 + 2 = 3
```

## About yf\_debug

`yf_debug` is a helper function if you don't use ipython, but python repl.

Usage:

```
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

```

## Compatibility

Python >= 3.5

