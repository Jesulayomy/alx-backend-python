#!/usr/bin/env python3
""" Asynchronous coroutine """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ An  asynchronous  coroutine wwaiting for an argument """

    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
