__author__ = 'Micheal Brady-Mahoney'

def getPricePerKw():
    price = int(input("Enter cents per kWh:"))
    price = float(price * 0.01)
    return price

def getDailyUse():
    dailyUse = float(input("Enter daily use in kWh:"))
    return dailyUse

def getBillingDays():
    billingDays = int(input("Enter number of billing days:"))
    return billingDays

print("Electricity bill estimator\n")
totalEstimate = getPricePerKw() * getDailyUse() * getBillingDays()
print("\nEstimated bill: ${:.2f} ".format(totalEstimate))