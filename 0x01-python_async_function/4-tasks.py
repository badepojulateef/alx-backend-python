#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function
task_wait_n. The code is nearly identical to wait_n except
task_wait_random is being called.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times
    with the specified max_delay.

    Args:
        n (int): The number of times to spawn the task_wait_random coroutine.
        max_delay (int): The maximum delay in seconds for each
        task_wait_random call.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
