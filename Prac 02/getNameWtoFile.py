__author__ = 'Micheal Brady-Mahoney'

nameFile = open("name.txt", "w")
name = input("Enter your name: ")
nameFile.write(name)
nameFile.close()