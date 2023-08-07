#!/usr/bin/env python3
""" multiple concurrency """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ waits for n then calls a wait random function """

    delays = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
