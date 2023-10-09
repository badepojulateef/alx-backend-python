#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named
wait_random that waits for a random delay between 0 and
max_delay (included and float value) seconds and eventually
returns it.

Use the random module.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay (inclusive).

    Args:
        max_delay (float, optional): The maximum
        delay in seconds (default is 10 seconds).

    Returns:
        float: The random delay that was generated and waited for.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
