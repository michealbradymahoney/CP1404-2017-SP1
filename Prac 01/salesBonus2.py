__author__ = 'Micheal Brady-Mahoney'

usersSales = float(input("Enter users sales: $"))
while usersSales >= 0:
    if usersSales < 1000:
        bonus = usersSales * 0.10
    else:
        bonus = usersSales * 0.15
    print("Your bonus is $ {:.2f} ".format(bonus))
    usersSales = float(input("Enter users sales: $"))
else:
    print("Have a nice day!")