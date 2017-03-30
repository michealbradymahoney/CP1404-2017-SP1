__author__ = 'Micheal Brady-Mahoney'

import random

line = []
no_of_games = int(input("How many quick picks? "))

for games in range(0, no_of_games):
    line = sorted([random.randint(1, 46) for i in range(0, 6)])
    print(line)

# TODO Make sure there are no duplicates. If so, generate new list
