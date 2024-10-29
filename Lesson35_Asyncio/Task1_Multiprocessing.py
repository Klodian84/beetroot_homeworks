from concurrent.futures import ProcessPoolExecutor

import time


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


#
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def square(n: int) -> int:
    return n * n


def cube(n: int) -> int:
    return n * n * n


def calculate_with_multiprocessing(numbers):
    with ProcessPoolExecutor() as executor:
        fib_results = list(executor.map(fibonacci, numbers))
        fac_results = list(executor.map(factorial, numbers))
        sq_results = list(executor.map(square, numbers))
        cb_results = list(executor.map(cube, numbers))
    return fib_results, fac_results, sq_results, cb_results


# Execute and time the multiprocessing code
numbers = list(range(1, 11))
start_time = time.time()
results = calculate_with_multiprocessing(numbers)
multiprocessing_time = time.time() - start_time

print(f"Multiprocessing execution time: {multiprocessing_time:.4f} seconds")
print("Results:", results)
