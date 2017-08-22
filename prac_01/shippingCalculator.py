__author__ = 'Micheal Brady-Mahoney'

numberItems = int(input("Number of items:"))
total = float(0)
while numberItems < 0:
    print("Invalid number of items")
    numberItems = int(input("Number of items:"))
else:
    for count in range (numberItems):
        price = float(input("Price of item: "))
        total+=price
    if total > 100:
        total*=.9
    print("Total price for " + str(numberItems) + " items is ${:.2f} ".format(total))
