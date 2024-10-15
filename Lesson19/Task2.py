def in_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if step == 0:
        raise ValueError("step argument must not be zero")

    if step > 0:
        while start < end:
            yield start
            start += step

    else:
        while start > end:
            yield start
            start += step


print(list(in_range(1, 10)))
