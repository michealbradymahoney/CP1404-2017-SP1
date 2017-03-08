__author__ = 'Micheal Brady-Mahoney'

import random
import string

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"
def password_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def main():
    permittedChars=''
    numberOfChars = input("How long a password? ")
    while (numberOfChars.isalpha() or len(numberOfChars) == 0 or numberOfChars.isspace()):
        print("***ERROR*** \n Enter only numbers")
        numberOfChars = input("How long a password? ")
    numberOfChars = int(numberOfChars)

    if (bool(input("Special characters required? "))):
        permittedChars += SPECIAL_CHARACTERS
    if (bool(input("Allow Uppercase Letters? "))):
        permittedChars += string.ascii_uppercase
    if (bool(input("Allow Lowercase Letters? "))):
        permittedChars += string.ascii_lowercase
    if (bool(input("Allow digit Letters? "))):
        permittedChars += string.digits

    print(password_generator(numberOfChars, permittedChars))




#userLength = int(input("Enter min length: "))
#specialCharsReq = bool(input("Special characters required? "))
#print("You generated password is: ", password)
main()

