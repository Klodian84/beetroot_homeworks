from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                raise ValueError(f"Cannot convert {result} to int")

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return str(result)
            except (ValueError, TypeError):
                raise ValueError(f"Cannot convert {result} to str")

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return bool(result)
            except (ValueError, TypeError):
                raise ValueError(f"Cannot convert {result} to bool")

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                raise ValueError(f"Cannot convert {result} to float")

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25  # Converts to int
assert do_something('True') is True  # Converts to bool
