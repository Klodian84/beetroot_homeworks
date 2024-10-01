#Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error.

def oops():
    raise IndexError ("This is an index error")

def handle_oops():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")

handle_oops()
