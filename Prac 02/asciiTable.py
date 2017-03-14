__author__ = 'Micheal Brady-Mahoney'

UPPER = 127
LOWER = 33
#
# character = str(input("Enter a character: "))
# print("The ASCII code for {} is {}".format(character, ord(character)))
#
# try:
#     while True:
#         number = int(input("Enter a number between %s and %s or any
#letter to quit: " % (LOWER, UPPER)))
#         if LOWER <= number <= UPPER:
#             print("The character for {} is {}".format(number, chr(number)))
#         else:
#             print("Error - Number must be between %s and %s " % (LOWER, UPPER))
# except ValueError:
#     print("Goodbye")

number_of_columns = int(input("Enter how many columns you'd like to display the values: "))
number_of_rows = (UPPER-LOWER+1)//number_of_columns
for i in range(number_of_rows):
    for j in range(number_of_columns):
        ascii_number = LOWER + (i * number_of_columns) + j
        # print("{:3},{:3} {}".format(i, j, chr(j)), end=" ")
        print("{:3} {}".format(ascii_number, chr(ascii_number)), end=" ")
    print()
ascii_number += 1
while ascii_number <= UPPER:
    print("{:3} {}".format(ascii_number, chr(ascii_number)), end=" ")
    ascii_number += 1
