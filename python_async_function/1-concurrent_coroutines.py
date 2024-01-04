#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays in ascending order"""
    delays = []
    tasks = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in tasks:
        delays.append(await task)
    return sorted(delays)
