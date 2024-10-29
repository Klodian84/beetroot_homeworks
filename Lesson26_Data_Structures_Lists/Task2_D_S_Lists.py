class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None  # Represents the top of the stack

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, otherwise False."""
        return self.head is None

    def push(self, item):
        """Pushes an item onto the stack."""
        new_node = Node(item)
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update head to the new node

    def pop(self):
        """Removes and returns the item from the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self.head.data
        self.head = self.head.next  # Move head to the next node
        return item

    def peek(self):
        """Returns the item at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data

    def __repr__(self):
        """Displays the stack elements from top to bottom."""
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        return "Stack(top -> bottom): " + " -> ".join(items)


stack = LinkedListStack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)  # Output: Stack(top -> bottom): 30 -> 20 -> 10

# Peek the top element
print("Top element:", stack.peek())  # Output: Top element: 30

# Pop elements from the stack
print("Popped element:", stack.pop())  # Output: Popped element: 30
print("Popped element:", stack.pop())  # Output: Popped element: 20
print(stack)  # Output: Stack(top -> bottom): 10

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

# Pop the last element
print("Popped element:", stack.pop())  # Output: Popped element: 10

# Check if the stack is empty after popping all elements
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? True
