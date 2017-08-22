__author__ = 'Micheal Brady-Mahoney'

# Below is to change the variables on the fly
MIN_LENGTH = int(input("Enter min length: "))
MAX_LENGTH = int(input("Enter max length: "))
SPECIAL_CHARS_REQUIRED = bool(input("Special characters required? "))

# Below is pre-set conditions
# MIN_LENGTH = 5
# MAX_LENGTH = 15
# SPECIAL_CHARS_REQUIRED = True

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"

def main():
    print("Please enter a valid password\n \
Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain: \n \
\t1 or more uppercase characters\n \
\t1 or more lowercase characters\n \
\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    length = len(password)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if (char.islower()):
            count_lower += 1
        elif (char.isupper()):
            count_upper += 1
        elif (char.isdigit()):
            count_digit += 1
    if SPECIAL_CHARS_REQUIRED:
        for char in password:
            if (char in SPECIAL_CHARACTERS):
                count_special += 1
        if count_special == 0:
            return False
    return True

main()