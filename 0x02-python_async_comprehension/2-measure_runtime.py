#!/usr/bin/env python3
""" This asynchronous function measures runtime of another Async Func """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures the runtime """

    start = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    elapsed = time.perf_counter() - start
    return elapsed
