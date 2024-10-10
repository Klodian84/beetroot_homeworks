
def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        all_args = args_str
        if kwargs_str:
            all_args += ", " + kwargs_str

        print(f"{func.__name__} called with {all_args}")


    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# Testing
add(4, 5)
square_all(2, 3, 4)

