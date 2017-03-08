__author__ = 'Micheal Brady-Mahoney'

def getTariff():
    TARIFF_11 = 0.244618
    TARIFF_31 = 0.136928
    tariff = int(input("Which tariff? 11 or 31:"))
    if tariff == 11:
        tariff = TARIFF_11
    else:
        tariff = TARIFF_31
    return tariff

def getDailyUse():
    dailyUse = float(input("Enter daily use in kWh:"))
    return dailyUse

def getBillingDays():
    billingDays = int(input("Enter number of billing days:"))
    return billingDays

print("Electricity bill estimator 2.0\n")
totalEstimate = getTariff() * getDailyUse() * getBillingDays()
print("\nEstimated bill: ${:.2f} ".format(totalEstimate))