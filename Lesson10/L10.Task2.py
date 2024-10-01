#Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def get_squared_division():
    try:
        a = float(input('Enter the first number (a): '))
        b = float(input('Enter the second number (b): '))

        if b == 0:
            raise ZeroDivisionError ("Division by zero is not valid.")

        result = (a ** 2 ) / b
        return result

    except ZeroDivisionError as e:
        print(f'Error: {e}')

    except ValueError:
        print("Error: Both inputs must be numbers.")

result = get_squared_division()
if result is not None:
    print(f'Result: {result}')