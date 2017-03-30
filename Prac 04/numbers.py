__author__ = 'Micheal Brady-Mahoney'

NUMBERS = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0] == 3
numbers[-1] == 2
numbers[3] == 1
numbers[:-1] == 3, 1, 4, 1, 5, 9
numbers[3:4] == 1
5 in numbers == True
7 in numbers == False
"3" in numbers == False
numbers + [6, 5, 3] == 3, 1, 4, 1, 5, 9, 2, 6, 5, 3
"""

"""
Write Python expressions (in the IDE) to achieve the following:
1. Change the first element of numbers to “ten”
2. Change the last element of numbers to 1
3. Get all the elements from numbers except the first two
4. Check if 9 is an element of numbers
"""


def q1():
    NUMBERS[0] = "ten"
    print(NUMBERS)


def q2():
    NUMBERS[-1] = 1
    print(NUMBERS)


def q3():
    print(NUMBERS[2:])


def q4():
    print(9 in NUMBERS)

q1()
q2()
q3()
q4()
