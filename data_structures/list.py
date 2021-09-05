from collections import *
import collections
'''
lista1 = [1,2,3,4,5]
lista2 = ["Wanderson","da","Cunha","Fontes"]
lista3 = ['Wanderson', 23, True]
'''
# Lists can contain data of different types.
# Data is organized and located through indexing

# print(lista2[0::3])
# Skip indices within the list [start:end:index]

#lista3[0]= 'Thiago'

'''
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[1][2])
#Prints the specified row and column on the screen
'''


print(50*'*','Creating and Adding Values ​​to List Structures',50*'*')
lista = ['Wanderson','Thiago', 'Navarro']
email = ['wancf19@gmail.com', 'wanderson@dataautomacao.com']

# Add a value to the end of the list
lista.append('Wanderson')
email.append('wancf19@gmail.com')

lista.insert(1,'Fontes')

# Enter value with a specific index from the list
# list(index,value)


lista.insert(1, 'da')

new_list = lista, email
print(lista)
print(new_list)#Exibição de uma lista dentro da outra


print('Size of list: LISTA(', len(lista), ')')# size of list
print('Size of list: NEW_LIST(', len(new_list), ')')

print('The DA data address is in the next position in the list:',lista.index('da'))# List rental address
print('The email address is in the following list position:',email.index('wancf19@gmail.com'))

print(50*'*','Removing elements from LISTS',50*'*')
# new_list.clear()    # DELETE ALL DATA WITHIN THE LIST
print(new_list)


new_list = lista.index('da', 0, 2)



print(new_list)
# Method to check whether the value is within the list or not
print('Cunha' in lista)
# Method to check how many times a data is repeated within the list
print(lista.count('da'))

num = [1, 2, 3, 5, 4, 7, 6, 8]
alf = ['a', 'c', 'b', 'e', 'd']
# Method for sorting values ​​in a list
alf.sort()
# SORTED(LISTA) Another way to put list values ​​in order
print(f'SORTED =  {sorted(num)}\nSORTED =  {alf}')
# RESVERSE attribute to revert list values
num.reverse()
print(f'REVERSE =  {num}!')

divisor = '*'
test = divisor.join(lista)
test1 = ' '.join(lista)
print(test)
print(test1)

# Methods Iterabbles
print('-'*100)

newList = ['Developer', 'Product Owner', 'DBA', 'Scrum Master', 'DevOps']
interable = iter(newList)
print('-- Functions Techs --\n')
try:
    print(next(interable))
    print(next(interable))
    print(next(interable))
    print(next(interable))
    print(next(interable))
    print(next(interable))
    print(next(interable))
except:
    pass
    # print('End')
finally:
    print('\nAll functions showed !')

# Read File
print('-'*100)
with open('data.txt', 'r') as filePointer:
    # Read lines from the file if it ends, it displays a blank line
    for row in iter(filePointer.readline, ''):
        print(row)

# Enumerate
print('-'*100)
for i, funct in enumerate(newList):
    print(i, funct)

# Zip
print('-'*100)
for f in zip(alf, newList):
    print(f)

# Collections
print('-'*50+'\nCollections')

# Count value in array
array = ['Wanderson', 'Aislan', 'Wanderson', 'Sassá', 'Gilna', 'Júlia', 'Júlia', 'Júlia', 'Geovana']
countValues = collections.defaultdict(int)
print(countValues)

countNames = Counter(array)
print(f'Number Júlia:       {countNames["Júlia"]}')
print(f'Number Wanderson:   {countNames["Wanderson"]}')
print(f'Number Geovana:     {countNames["Geovana"]}')
print(f'Number Aurizete:    {countNames["Aurizete"]}')

print('-'*50+f'\nThe amount names: {sum(countNames.values())}')
print('-'*50+f'\nThe amount names more common: {countNames.most_common(3)}')
print('-'*50+f'\nThe amount names more common: {countNames.most_common()}')













