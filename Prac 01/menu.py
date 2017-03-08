__author__ = 'Micheal Brady-Mahoney'

name = input("Enter name: ")
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello " + name)
    elif choice == "G":
        print("Goodbye " + name)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")