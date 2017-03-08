__author__ = 'Micheal Brady-Mahoney'

# lower = input("Enter a lower number: ")
# upper = input("Enter an upper number: ")
# print("Enter a number (" + str.format(lower) + "-" + str.format(upper) + "):")

for i in range(33, 126, 1):
    print("{:>3} {:<4}".format(i, chr(i)))