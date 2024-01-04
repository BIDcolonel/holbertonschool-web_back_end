#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The task at hand involves measuring the runtime of the async_comprehension
function, which generates 10 random numbers using an async generator, in
parallel four times using asyncio.gather.

The async_comprehension function uses an async generator that yields 10
random numbers. This generator, async_generator, sleeps for 1 second between
each yield, simulating some form of asynchronous delay.

When async_comprehension is executed once, it awaits the completion of the
async generator, which takes roughly 10 seconds to yield 10 random numbers
(1 second sleep between each number for 10 numbers).

The measure_runtime function then executes async_comprehension four times in
parallel using asyncio.gather. Despite the tasks running in parallel, they
do not complete simultaneously due to the async nature of the generator.
Each call to async_comprehension will take roughly 10 seconds to execute,
resulting in a total runtime of around 10 seconds for all four executions
due to their parallel nature.

So, although these tasks run concurrently, the overall runtime is not reduced
because each task individually takes about 10 seconds to complete due to
the 1-second sleep in the async generator."""
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
