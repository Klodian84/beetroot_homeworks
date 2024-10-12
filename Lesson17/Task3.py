from math import gcd


class Fraction:
    def __init__(self, value):
        # If the input is a float or decimal, convert it into a fraction
        if isinstance(value, float):
            num, den = str(value).split(".")
            self.numerator = int(num)
            self.denominator = 10 ** len(den)
        elif isinstance(value, int):
            self.numerator = value
            self.denominator = 1
        elif isinstance(value, tuple) and len(value) == 2:
            self.numerator, self.denominator = value
        else:
            raise ValueError(
                "Invalid input. Fraction should be represented as a tuple (numerator, denominator) or float or int.")

        # Simplify the fraction
        self.simplify()

    def simplify(self):
        """Simplify the fraction to its lowest terms."""
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        # If denominator is negative, move the sign to the numerator
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __repr__(self):
        return f"Fraction({self.numerator}/{self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be of type 'Fraction'.")
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction((new_numerator, new_denominator))

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be of type 'Fraction'.")
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction((new_numerator, new_denominator))

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be of type 'Fraction'.")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction((new_numerator, new_denominator))

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be of type 'Fraction'.")
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with a numerator of zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction((new_numerator, new_denominator))

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Operands must be of type 'Fraction'.")
        return self.numerator * other.denominator == other.numerator * self.denominator


# Example usage:
x = Fraction((1, 2))  # 1/2
y = Fraction((1, 4))  # 1/4

# Addition
print(x + y)  # Fraction(3/4)

# Subtraction
print(x - y)  # Fraction(1/4)

# Multiplication
print(x * y)  # Fraction(1/8)

# Division
print(x / y)  # Fraction(2/1)

# Equality check
print(x + y == Fraction((3, 4)))  # True
