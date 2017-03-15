__author__ = 'Micheal Brady-Mahoney'

score = float(input("Enter score: "))
while -1 <= score < 101:
    if 50 < score < 89:
        print("Passable")
    elif 90 < score <= 100:
        print("Excellent")
    else:
        print("Bad")
    break
else:
    print("Invalid score")

