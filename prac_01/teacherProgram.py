__author__ = 'Micheal Brady-Mahoney'

MENU = "***MENU****\n(A)Show the even numbers from x to y\n(B)Show the odd numbers from x to y \
\n(C)Show the squares from x to y\n(Q)Quit\n"

x = int(input("Enter a number for X= "))
y = int(input("Enter a number for Y= "))

print(MENU)

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "A":
        odd = [x for x in range(x, y+1) if x % 2 == 0]
        print(odd, end=' ')
        print()
    elif choice == "B":
        even = [x for x in range(x, y+1) if x % 2 == 1]
        print(even, end=' ')
        print()
    elif choice == "C":
        # TODO Find out what the below means
        print("Show the squares from x to y")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")