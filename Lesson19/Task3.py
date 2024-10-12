class CustomIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.data):
            result = self.data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        if isinstance(index, int):
            # Access single item
            if 0 <= index < len(self.data):
                return self.data[index]
            else:
                raise IndexError("Index out of range.")
        elif isinstance(index, slice):
            # Handle slicing (start:stop:step)
            return self.data[index]
        else:
            raise TypeError("Invalid index type, must be int or slice.")


custom_iterable = CustomIterable([10, 20, 30, 40, 50])

for item in custom_iterable:
    print(item)

print(custom_iterable[0])
print(custom_iterable[1])

print(custom_iterable[1:6])
