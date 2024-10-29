import math

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


NUMBERS = [
    2, 1099726899285419, 1570341764013157, 1637027521802551, 1880450821379411,
    1893530391196711, 2447109360961063, 3, 2772290760589219, 3033700317376073,
    4350190374376723, 4350190491008389, 4350190491008390, 4350222956688319,
    2447120421950803, 5
]


def filter_primes_threadpool(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [n for n, prime in zip(numbers, results) if prime]


def filter_primes_processpool(numbers):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [n for n, prime in zip(numbers, results) if prime]


def main():
    start = time.time()
    threadpool_primes = filter_primes_threadpool(NUMBERS)
    threadpool_time = time.time() - start

    start = time.time()
    processpool_primes = filter_primes_processpool(NUMBERS)
    processpool_time = time.time() - start

    # Output results and performance comparison
    print("Primes found with ThreadPoolExecutor:", threadpool_primes)
    print(f"ThreadPoolExecutor took {threadpool_time:.4f} seconds")

    print("Primes found with ProcessPoolExecutor:", processpool_primes)
    print(f"ProcessPoolExecutor took {processpool_time:.4f} seconds")

    assert threadpool_primes == processpool_primes, "Results are inconsistent between methods!"


if __name__ == '__main__':
    main()

# ProcessPoolExecutor took 2.2620 seconds
