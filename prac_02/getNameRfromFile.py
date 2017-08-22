__author__ = 'Micheal Brady-Mahoney'

nameFile = open("name.txt", "r")
name = nameFile.read().strip()
print("Your name is", name)
nameFile.close()