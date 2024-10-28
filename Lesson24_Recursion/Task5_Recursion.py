def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")

    if len(digit_string) == 0:
        return 0

    return int(digit_string[0]) + sum_of_digits(digit_string[1:])
