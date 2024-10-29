class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None  # Front of the queue
        self.tail = None  # Back of the queue

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, otherwise False."""
        return self.head is None

    def enqueue(self, item):
        """Adds an item to the back of the queue."""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node  # Queue was empty, head points to new node
            self.tail = new_node  # Tail also points to the new node
        else:
            self.tail.next = new_node  # Link the old tail to the new node
            self.tail = new_node  # Update the tail to the new node

    def dequeue(self):
        """Removes and returns the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.head.data
        self.head = self.head.next  # Move head to the next node
        if self.head is None:
            self.tail = None  # If the queue is now empty, update tail to None
        return item

    def peek(self):
        """Returns the item at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.head.data

    def __repr__(self):
        """Displays the queue elements from front to back."""
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        return "Queue(front -> back): " + " -> ".join(items)


queue = LinkedListQueue()

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue)  # Output: Queue(front -> back): 10 -> 20 -> 30

# Peek at the front element
print("Front element:", queue.peek())  # Output: Front element: 10

# Dequeue elements from the queue
print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 10
print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 20
print(queue)  # Output: Queue(front -> back): 30

# Check if the queue is empty
print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False

# Dequeue the last element
print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 30

# Check if the queue is empty after dequeuing all elements
print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? True

# Output

# Queue(front -> back): 10 -> 20 -> 30
# Front element: 10
# Dequeued element: 10
# Dequeued element: 20
# Queue(front -> back): 30
# Is queue empty? False
# Dequeued element: 30
# Is queue empty? True
