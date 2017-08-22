"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

__author__ = 'Micheal Brady-Mahoney'

usersSales = float(input("Enter users sales: $"))
bonus = 0
if usersSales < 1000:
    bonus = usersSales * 0.10
else:
    bonus = usersSales * 0.15
print("Your bonus is $ {:.2f} ".format(bonus))