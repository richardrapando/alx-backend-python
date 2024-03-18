#!/usr/bin/env python3
'''basics of async
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random delay between 0 and max_delay (included and float value) seconds
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
