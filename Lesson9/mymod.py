# mymod.py

def count_lines(name):
    """Returns the number of lines in the given file."""
    with open(name, 'r') as f:
        return len(f.readlines())

def count_chars(name):
    """Returns the number of characters in the given file."""
    with open(name, 'r') as f:
        return len(f.read())

def test(name):
    """Calls both count_lines and count_chars and prints the results."""
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"{name} has {lines} lines and {chars} characters.")
