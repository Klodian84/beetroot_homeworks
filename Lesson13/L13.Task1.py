

def count_local_variables(func):
    return func.__code__.co_nlocals

def example_function():
    x = 5
    y = 6
    z = x + y

#  We call the function to count local variables in example_function

num_locals = count_local_variables(example_function)
print(f"Number of local variables in 'example_function': {num_locals}")
