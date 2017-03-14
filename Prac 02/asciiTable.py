__author__ = 'Micheal Brady-Mahoney'

UPPER = 127
LOWER = 33

character = str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(character, ord(character)))

try:
    while True:
        number = int(input("Enter a number between %s and %s or any letter to quit: " % (LOWER, UPPER)))
        if LOWER <= number <= UPPER:
            print("The character for {} is {}".format(number, chr(number)))
        else:
            print("Error - Number must be between %s and %s " % (LOWER, UPPER))
except ValueError:
    print("Goodbye")
