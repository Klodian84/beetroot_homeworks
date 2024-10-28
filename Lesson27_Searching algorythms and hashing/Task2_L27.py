from typing import List, Optional


def fibonacci_search(arr: List[int], target: int) -> Optional[int]:
    n = len(arr)

    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:

        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i


        elif arr[i] > target:
            fib = fib2
            fib1 -= fib2
            fib2 = fib - fib1


        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return None


arr = [10, 22, 35, 40, 45, 50, 70, 82, 85, 95]
target = 85
result = fibonacci_search(arr, target)

if result is not None:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found.")
