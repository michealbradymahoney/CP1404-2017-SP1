__author__ = 'Micheal Brady-Mahoney'

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

# word_format = str(input("Enter word format. \nC - Consonant \nV - Vowel \n>>>").lower())
# word = ""
# for kind in word_format:
#     if kind == "c":
#         word += random.choice(CONSONANTS)
#     else:
#         word += random.choice(VOWELS)
#
# print(word)

OPTIONS = 'c' + 'v'
word_format = ""
word = ""
numLetters = int(input("How many letter word would you like?"))
for i in range(numLetters):
        word_format += random.choice(OPTIONS)
print(word_format)
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)