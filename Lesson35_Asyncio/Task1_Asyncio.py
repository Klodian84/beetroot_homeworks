import asyncio
import time
from typing import List


async def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


async def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


async def square(n: int) -> int:
    return n * n


async def cube(n: int) -> int:
    return n * n * n


async def main_async(numbers: List[int]):
    fib_results = await asyncio.gather(*(fibonacci(n) for n in numbers))
    fac_results = await asyncio.gather(*(factorial(n) for n in numbers))
    sq_results = await asyncio.gather(*(square(n) for n in numbers))
    cb_results = await asyncio.gather(*(cube(n) for n in numbers))

    return fib_results, fac_results, sq_results, cb_results


# Timing
start_time = time.time()
asyncio.run(main_async(list(range(1, 11))))
async_time = time.time() - start_time
print(f"Asynchronous execution time: {async_time:.4f} seconds")


