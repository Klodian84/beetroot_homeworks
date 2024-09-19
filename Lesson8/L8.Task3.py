# A simple calculator.

# Create a function called make_operation,
# which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be '+', '-' or '*')
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.

def make_operation(operator, *args):
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
    else:
        result = None
    return result


print(make_operation('+', 7, 7, 2))
