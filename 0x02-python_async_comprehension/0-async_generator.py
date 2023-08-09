#!/usr/bin/env python3
""" an async generator function """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ loops and generate a random number for 10 cycles """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
