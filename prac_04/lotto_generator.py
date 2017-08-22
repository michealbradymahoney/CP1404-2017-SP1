__author__ = 'Micheal Brady-Mahoney'

import random

no_of_games = int(input("How many quick picks? "))

for games in range(0, no_of_games):
    line = []
    for i in range(0, 6):
        generated_number = random.randint(1, 45)
        while generated_number in line:
            generated_number = random.randint(1, 45)
        line.append(generated_number)
    print(*(sorted(line)), sep=' ')

