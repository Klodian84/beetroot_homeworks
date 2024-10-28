class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update value if key exists
                return

        self.table[index].append((key, value))
        self.count += 1

    def remove(self, key):

        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]

                self.count -= 1
                return
        raise KeyError(f"Key {key} not found.")

    def __contains__(self, key):
        index = self._hash(key)
        return any(k == key for k, _ in self.table[index])

    def __len__(self):
        return self.count

    def get(self, key, default=None):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return default


hash_table = HashTable()

hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

print(len(hash_table))  # Output: 3

print("apple" in hash_table)  # Output: True
print("grape" in hash_table)  # Output: False

hash_table.remove("banana")
print(len(hash_table))  # Output: 2
print("banana" in hash_table)  # Output: False
