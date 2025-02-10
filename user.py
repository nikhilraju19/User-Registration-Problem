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

def email_id():
    email = input("Enter your email id: ")
    pattern = r'^[a-zA-Z0-9+%_-]+(?:\.[a-zA-Z0-9+%_-]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
    while True:
        search = re.fullmatch(pattern, email)
        if search:
            logging.info(f"{email} is valid email id")
            print(f"{email} is a valid email id")
            return email
        else:
            logging.info(f"{email} is valid email id")
            print("Please enter a valid email id")

def last_name():
    pattern = r'^[A-Z][a-z]{2,}$'
    while True:
        valid_last_name = input("Enter your last name: ")
        search = re.fullmatch(pattern,valid_last_name)
        if search:
            logging.info(f"{valid_last_name} is a valid last name")
            return valid_last_name
        else:
            logging.warning(f"{valid_last_name} is a invalid last name. Please enter a valid last name")
            print("Please enter valid last name")

def first_name():
    pattern = r'^[A-Z][a-z]{2,}(?: [A-Z][a-z]+){0,2}$'
    while True:
        valid_first_name = input("Enter your first name: ")
        search = re.fullmatch(pattern,valid_first_name)
        if search:
            logging.info(f"{valid_first_name} is a valid first name")
            return valid_first_name
        else:
            logging.warning(f"{valid_first_name} is a invalid first name. Please enter a valid first name")
            print("Please enter valid first name")

if __name__ == "__main__":
    first_name()
    last_name()
    email_id()
