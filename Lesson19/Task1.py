def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


for index, value in with_index(['a', 'b', 'c'], start=1):
    print(index, value)
