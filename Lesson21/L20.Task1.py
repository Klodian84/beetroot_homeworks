import logging

logging.basicConfig(filename="file_manager.log", level=logging.INFO, format="%(asctime)s - %(message)s")


class FileContextManager:
    _open_count = 0

    def __init__(self, file_name, mode):
        """Initialize with the file name and mode."""
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Enter the runtime context and open the file."""
        try:

            self.file = open(self.file_name, self.mode)
            FileContextManager._open_count += 1
            logging.info(f"Opened file '{self.file_name}' in '{self.mode}' mode.")
            return self.file
        except Exception as e:
            logging.error(f"Error while opening the file: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context, close the file, and handle exceptions if any."""
        try:
            if self.file:
                self.file.close()  # Ensure the file is properly closed
                logging.info(f"Closed file '{self.file_name}'.")
        except Exception as e:
            logging.error(f"Error while closing the file: {e}")

        if exc_type is not None:
            logging.error(f"Exception occurred: {exc_type}, {exc_val}")

            return False

        return True

    @classmethod
    def get_open_count(cls):
        """Return the number of times files have been opened."""
        return cls._open_count


if __name__ == "__main__":
    try:

        with FileContextManager("example.txt", "w") as f:
            f.write("Hello, this is a test file.")

        with FileContextManager("example.txt", "r") as f:
            content = f.read()
            print(content)


        print(f"Files have been opened {FileContextManager.get_open_count()} times.")
    except Exception as e:
        print(f"An error occurred: {e}")
