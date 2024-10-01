
#  What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise KeyError ("This is a Key Error")

def handle_oops():
    try:
        oops()

    except IndexError as e:
        print(f"Caught an  Error {e}")

handle_oops()