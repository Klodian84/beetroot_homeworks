class CustomException(Exception):
    def __init__(self, msg):

        super().__init__(msg)


        with open("logs.txt", "a") as log_file:
            log_file.write(f"Error: {msg}\n")
