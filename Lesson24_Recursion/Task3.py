def mult(a: int, n: int) -> int:

    if n < 0:
        raise ValueError("This function works only with positive integers")

    if n == 0:
        return 0

    return a + mult(a, n - 1)
