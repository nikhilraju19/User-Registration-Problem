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

def first_name():
    pattern = r'^[A-Z][a-z]{2,}(?: [A-Z][a-z]+){0,2}$'
    while True:
        first_name = input("Enter your first name: ")
        search = re.search(pattern,first_name)
        if search:
            logging.info(f"{first_name} is a valid first name")
            print(f"{first_name} is a valid first name")
            return first_name
        else:
            logging.warning(f"{first_name} is a invalid first name. Please enter a valid first name")
            print("Please enter  valid first name")

if __name__ == "__main__":
    first_name()
