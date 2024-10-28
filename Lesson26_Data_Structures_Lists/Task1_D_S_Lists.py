class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, item) -> bool:
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current:
            if current.data == item:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        raise ValueError(f"Item {item} not found in the list")

    # Additional methods

    def append(self, item):
        """Appends an item at the end of the list."""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def index(self, item) -> int:
        """Returns the index of the item in the list."""
        current = self.head
        idx = 0
        while current:
            if current.data == item:
                return idx
            current = current.next
            idx += 1
        raise ValueError(f"Item {item} not found in the list")

    def pop(self, position=None):
        """Removes and returns the item at the given position or the last item if position is None."""
        if self.is_empty():
            raise IndexError("pop from empty list")

        current = self.head
        previous = None
        idx = 0

        if position is None:
            # Find last item
            while current.next:
                previous = current
                current = current.next
            if previous:
                previous.next = None
            else:
                self.head = None
            return current.data

        # If position is specified, find the item at that position
        while current:
            if idx == position:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return current.data
            previous = current
            current = current.next
            idx += 1

        raise IndexError("pop index out of range")

    def insert(self, position: int, item):
        """Inserts an item at the given position."""
        if position < 0 or position > self.size():
            raise IndexError("insert index out of range")

        new_node = Node(item)
        current = self.head
        previous = None
        idx = 0

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        while idx < position:
            previous = current
            current = current.next
            idx += 1

        previous.next = new_node
        new_node.next = current

    def slice(self, start: int, stop: int):
        """Returns a new list containing elements from start up to but not including stop."""
        if start < 0 or stop > self.size() or start > stop:
            raise IndexError("slice indices out of range")

        sliced_list = UnorderedList()
        current = self.head
        idx = 0

        while current and idx < stop:
            if idx >= start:
                sliced_list.append(current.data)
            current = current.next
            idx += 1

        return sliced_list

    def __repr__(self):
        """Utility method to display the list items."""
        current = self.head
        items = []
        while current:
            items.append(current.data)
            current = current.next
        return "UnorderedList([" + ", ".join(map(str, items)) + "])"


# Create an UnorderedList and add some elements
ul = UnorderedList()
ul.add(1)
ul.add(2)
ul.add(3)
ul.append(4)

# Display list
print("Original list:", ul)

# Insert an element at position 1
ul.insert(1, 5)
print("After insert:", ul)

# Pop an element at position 2
popped = ul.pop(2)
print("Popped element:", popped)
print("After pop:", ul)

# Index of element
idx = ul.index(4)
print("Index of 4:", idx)

# Slice of list from index 1 to 3
sliced = ul.slice(1, 3)
print("Sliced list from 1 to 3:", sliced)
