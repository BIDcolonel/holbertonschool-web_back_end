#!/usr/bin/env python3
"""Returns a list of delays in ascending order of float values of the
    delays randomly generated from task_wait_random function in async"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines concurrently using asyncio.gather."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
