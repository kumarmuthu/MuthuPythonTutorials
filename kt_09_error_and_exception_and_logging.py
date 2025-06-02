# Python assert
# x = "hello"
# if x != 'hello':
#     raise Exception("Sriram given this exception")
#
# #if condition returns True, then nothing happens:
# assert x == "hello1", f"It must match with '{x}'"


# Python Try, Except, else, finally
"""
try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
"""
import datetime
import time
import os

get_cwd = os.getcwd()

# Example-1
try:
    fh = open(rf"{get_cwd}\Log\testfile", "w")
    fh.write("This is my test file for exception handling!!")
except FileNotFoundError:
    print("Error: exception with FileNotFoundError")
except IOError:
    print("Error: can\'t find file or read data")
except Exception as Err:
    print(f"Unknown Exception!: {Err}")
else:
    print("Written content in the file successfully")
    fh.close()
finally:
    print("From Finally block")
print("End")

# Example-2
try:
    file = open(rf"{get_cwd}\Log\example.txt", "r")
    content = file.read()
    print(f"Content: {content}")
except FileNotFoundError:
    print("Error: The file was not found.")
else:
    print("File read operation successful.")
finally:
    if 'file' in locals():
        file.close()
    print("File operation is complete.")


# Custom exception
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 18 and 100"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Provided age: {self.age}"


def set_age(age):
    if age < 18 or age > 100:
        raise InvalidAgeError(age)
    print(f"Age is set to {age}")


try:
    set_age(150)
except InvalidAgeError as e:
    print(f"Invalid age: {e.age}. {e.message}")

# Logging in Python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Example usage
def calculate_sum(a, b):
    time.sleep(5)
    logging.debug(f"Calculating sum of {a} and {b}")
    result = a + b
    logging.info(f"Sum calculated successfully: {result}")
    time.sleep(3)
    return result


# Main program
if __name__ == "__main__":
    from datetime import datetime

    now = datetime.now()
    print("Now time:", now)
    logging.info("Starting the program")

    current_time = now.strftime("%H:%M:%S")
    print("Start Time =", current_time)
    result = calculate_sum(10, 20)
    logging.info("Program completed")
    end_time = now.strftime("%H:%M:%S")
    print("End Time =", end_time)
