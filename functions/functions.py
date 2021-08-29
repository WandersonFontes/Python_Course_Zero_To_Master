def name():
    name = str(input('Hello! Whats your name? '))
    print(f'Welcome {name}!')
# name()


def sum(num1, num2):
    result = num1 + num2
    print(f'Result: {result}.')
# positional arguments
# sum(1, 1)

# keyword arguments
# sum(num1=1, num2=2)
# sum(num2=1, num1=2)


def sub(num1, num2):
    return num1 - num2
# print(f'Result is {sub(4, 3)}.')

# Methods vs Functions

# Methods
# print()
# list()
# count()
# input()

# Functions
def new_function():
    print("I'm one function")
# new_function()


def myCreator():
    # DocStrings
    '''
    Info: Code creator declaration function
    '''
    print('WanDEV')
# show Info: Code creator declaration function


myCreator()
# help(myCreator)
# print(myCreator.__doc__)


def super_function_arg(*args):
    print(args)
# super_function_arg('TEST1', 'TEST2', 'TEST3')


def super_function_kwargs(**kwargs):
    for itens in kwargs.values():
        print(itens)
    print(kwargs)


super_function_kwargs(test1='TEST1', test2='TEST2', test3='TEST3')

# Functions Transformers
num = (1,2,3,4,5,6,7,8,9)


def getNumberOdd(numbres):
    if numbres%2 == 0:
        return False
    return True

def higherNumber(numbers):
    if numbers == 1:
        return False
    return True

def pontecy(numbers):
    return numbers**2



odd = list(filter(getNumberOdd, num))
print(odd)

higher = list(filter(higherNumber, num))
print(higher)

potentiation = list(map(pontecy, num))
print(potentiation)
