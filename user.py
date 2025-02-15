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

def password():
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=(?:[^!@#$%^&*()\-+]*[!@#$%^&*()\-+][^!@#$%^&*()\-+]*)$).{8,}$'
    while True:
        final_password = input("Enter your password (min 8 characters, >=1 [A-Z], >=1 [0-9] and ==1 special character ): ")
        search = re.fullmatch(pattern, final_password)
        if search:
            logging.info(f"{final_password} is a valid password")
            print(f"{final_password} is a valid password")
            return final_password
        else:
            logging.warning(f"{final_password} is a invalid password")
            print("Please enter a valid password (min 8 characters, >=1 [A-Z], >=1 [0-9] and ==1 special character )")

def mobile_number():
    pattern = r'^\+[0-9]{2,3} [0-9]{10}$'
    while True:
        mobile_no = input("Enter your mobile number: ")
        search = re.fullmatch(pattern, mobile_no)
        if search:
            logging.info(f"{mobile_no} is valid mobile number")
            return mobile_no
        else:
            logging.warning(f"{mobile_no} is a invalid mobile number")
            print("Please enter a valid mobile number")
            
def email_id():
    pattern = r' ^[a-zA-Z0-9+%_-]+(?:\.[a-zA-Z0-9+%_-]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$ '
    while True:
        email = input("Enter your email id: ")
        search = re.fullmatch(pattern, email)
        if search:
            logging.info(f"{email} is valid email id")
            return email
        else:
            logging.warning(f"{email} is invalid email id")
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
            
def main():
    first_name()
    last_name()
    email_id()
    mobile_number()
    password()

if __name__ == "__main__":
    main()
    