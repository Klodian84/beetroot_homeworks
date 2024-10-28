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


def is_balanced(sequence: str) -> bool:
    stack = Stack()
    # Dictionary to match opening and closing brackets
    brackets = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in brackets.values():  # If it's an opening bracket
            stack.push(char)
        elif char in brackets:  # If it's a closing bracket
            if stack.is_empty() or stack.pop() != brackets[char]:
                return False

    # If the stack is empty, all brackets were matched
    return stack.is_empty()


sequence = input("Enter a sequence of characters: ")
if is_balanced(sequence):
    print("The sequence is balanced.")
else:
    print("The sequence is not balanced.")

# Enter a sequence of characters: {[()]}
# The sequence is balanced.
#
# Enter a sequence of characters: {[(])}
# The sequence is not balanced.
