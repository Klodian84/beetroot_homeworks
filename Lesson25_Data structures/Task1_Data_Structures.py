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

    def size(self) -> int:
        return len(self.items)


def reverse_sequence(sequence: str) -> str:
    stack = Stack()

    # Push each character onto the stack
    for char in sequence:
        stack.push(char)

    # Pop characters from the stack to get them in reverse order
    reversed_sequence = ""
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    return reversed_sequence


sequence = input("Enter a sequence of characters: ")  # klodi
reversed_sequence = reverse_sequence(sequence)
print("Reversed sequence:", reversed_sequence)  # idolk
