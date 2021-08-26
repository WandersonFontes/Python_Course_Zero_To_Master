# Python Enhancement Proposal
# PEP 20 -> ZEN of Python

# PEP 8 -> Code structuring and formatting

# Import always on top and each on a single line
from random import randrange

# print(randrange(3, 5))

# 4 blank spaces must be used to consolidate indentation


class NewClass:
    def newTest(self):
        print('My test')

    if 1 == 1:
        print("True")
# my = myClass()
# my.test()

# Code lines limit 79 lines


print(len('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'))

# Limit of lines comments or docstrings 72
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Separation of classes and methods will be two blank lines


class FristClass:
    def __init__(self):
        print('1ª')


class SecondClass:
    def __init__(self):
        print('2ª')

# Class methods are separated by a blank line


class Game:
    def start(self):
        print('Start')

    def stop(self):
        print('Stop')

    def exit(self):
        print('Exit')