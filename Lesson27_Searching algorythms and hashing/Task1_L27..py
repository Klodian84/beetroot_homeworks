from typing import List, Optional


def binary_search_recursive(arr: List[int], target: int, low: int, high: int) -> Optional[int]:
    if low > high:
        return None
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search_recursive(arr, target, low=0, high=len(arr) - 1)

if result is not None:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found.")
