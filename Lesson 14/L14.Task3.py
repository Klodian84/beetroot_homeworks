def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            argument = args[0]

            if not isinstance(argument, type_):
                print(f"Argument must be of type {type_.__name__}")
                return False

            if len(argument) > max_length:
                print(f"Argument exceeds max length of {max_length}")
                return False

            # Check if the argument contains all required symbols
            for symbol in contains:
                if symbol not in argument:
                    print(f"Argument does not contain required symbol: {symbol}")
                    return False

            # If all checks pass, call the original function
            return func(*args, **kwargs)

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

