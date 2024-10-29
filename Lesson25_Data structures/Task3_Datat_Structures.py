class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def get_from_stack(self, e):
        temp_stack = Stack()
        found_item = None

        # Transfer elements to temp_stack until we find e or the stack is empty
        while not self.is_empty():
            item = self.pop()
            if item == e:
                found_item = item
                break
            else:
                temp_stack.push(item)

        # Return elements from temp_stack back to the original stack to maintain order
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found_item is None:
            raise ValueError(f"Element {e} not found in stack")

        return found_item


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def get_from_queue(self, e):
        size = len(self.items)
        found_item = None

        for i in range(size):
            item = self.dequeue()
            if item == e and found_item is None:
                found_item = item
            else:
                self.enqueue(item)

        if found_item is None:
            raise ValueError(f"Element {e} not found in queue")

        return found_item


# Stack usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.get_from_stack(2))  # Output: 2
# stack.get_from_stack(4)  # Raises ValueError

# Queue usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.get_from_queue(2))  # Output: 2
# queue.get_from_queue(4)  # Raises ValueError




