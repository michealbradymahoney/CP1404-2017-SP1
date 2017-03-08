__author__ = 'Micheal Brady-Mahoney'

numberFile = open("numbers.txt")
firstNumber = int(numberFile.readline())
secondNumber = int(numberFile.readline())
print(firstNumber + secondNumber)
numberFile.close()

numberFile = open("numbers.txt")
total = 0
for line in numberFile:
    number = int(line)
    total = total + number
print(total)
numberFile.close()