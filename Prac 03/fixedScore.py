__author__ = 'Micheal Brady-Mahoney'


def get_score():
    grade = float(input("Enter score: "))
    return grade


def main():
    score = get_score()
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


main()

