__author__ = 'Micheal Brady-Mahoney'

# character = str(input("Enter a character: "))
# print("The ASCII code for {} is {}".format(character, ord(character)))

# UPPER = 0
# LOWER = 0


def get_lower_upper():
    lower = int(input("Enter a lower number between 33 and 127:"))
    while lower < 33 or lower > 127:
        print("Please enter a valid number!")
        lower = int(input("Enter a lower number between 33 and 127:"))
    upper = int(input("Enter an upper number between {} and 127:".format(lower)))
    while upper < lower or upper > 127:
        print("Please enter a valid number!")
        upper = int(input("Enter an upper number between {} and 127:".format(lower)))
    return lower, upper


def main():
    min_num, max_num = get_lower_upper()
    number = int(input("Enter a number between %s and %s or any letter to quit: " % (min_num, max_num)))
    while number < min_num or number > max_num:
        print("Error - Number must be between %s and %s " % (min_num, max_num))
        number = int(input("Enter a number between %s and %s or any letter to quit: " % (min_num, max_num)))
    print("The character for {} is {}".format(number, chr(number)))


main()

# try:
#     while True:
#         a, b = get_lower_upper()
#         number = int(input("Enter a number between %s and %s or any letter to quit: " % (a, b)))
#         if LOWER <= number <= UPPER:
#             print("The character for {} is {}".format(number, chr(number)))
#         else:
#             print("Error - Number must be between %s and %s " % (LOWER, UPPER))
# except ValueError:
#     print("Goodbye")

# UPPER = 127
# LOWER = 33
# number_of_columns = int(input("Enter how many columns you'd like to display the values: "))
# number_of_rows = (UPPER-LOWER+1)//number_of_columns
# for i in range(number_of_rows):
#     for j in range(number_of_columns):
#         ascii_number = LOWER + (i * number_of_columns) + j
#         # print("{:3},{:3} {}".format(i, j, chr(j)), end=" ")
#         print("{:3} {}".format(ascii_number, chr(ascii_number)), end=" ")
#     print()
# ascii_number += 1
# while ascii_number <= UPPER:
#     print("{:3} {}".format(ascii_number, chr(ascii_number)), end=" ")
#     ascii_number += 1
