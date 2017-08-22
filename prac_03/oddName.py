__author__ = 'Micheal Brady-Mahoney'

'''Micheal Brady-Mahoney'''
def main():
    name = input(str("Enter your name:"))
    count = 0
    if name.isalpha():
        for char in name:
            if count % 2 != 0:
                print(char)
                count += 1
            else:
                count += 1
    else:
        print("Error")
        name = input(str("Enter your name:"))

main()