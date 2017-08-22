__author__ = 'Micheal Brady-Mahoney'

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!" )
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions
# 1.    When will a ValueError occur?
#       When a character other than a number is entered
# 2.    When will a ZeroDivisionError occur?
#       When zero is entered as the denominator
# 3.    Could you change  the code to avoid the possibility of a ZeroDivisionError?
#       You could put an error checking loop in, if the user enters a zero is displays an error message and ask to \
#       input again
