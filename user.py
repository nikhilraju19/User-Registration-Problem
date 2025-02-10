import re
import logging

#Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : %(levelname)s : %(message)s',
    handlers = [
		logging.FileHandler('sample.log'),
		logging.StreamHandler()
	])

def last_name():
    pattern = r'^[A-Z][a-z]{2,}$'
    while True:
        last_name = input("Enter your last name: ")
        search = re.fullmatch(pattern,last_name)
        if search:
            logging.info(f"{last_name} is a valid last name")
            print(f"{last_name} is a valid last name")
            return last_name
        else:
            logging.warning(f"{last_name} is a invalid last name. Please enter a valid last name")
            print("Please enter  valid last name")

def first_name():
    pattern = r'^[A-Z][a-z]{2,}(?: [A-Z][a-z]+){0,2}$'
    while True:
        first_name = input("Enter your first name: ")
        search = re.fullmatch(pattern,first_name)
        if search:
            logging.info(f"{first_name} is a valid first name")
            return first_name
        else:
            logging.warning(f"{first_name} is a invalid first name. Please enter a valid first name")
            print("Please enter  valid first name")

if __name__ == "__main__":
    first_name()
    last_name()
