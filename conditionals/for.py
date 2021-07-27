
'''
i = 0
for i in range(11):
    for x in ['a','b','c','d']:
        print(i,x)

cad ={
    'name ': 'Wanderson',
    'age  ':1996,
    'magic':True
}
for key,value in cad.items():
    print(key,":",value)


# compiler
#counter(contador) recebe a soma do indice da lista
my_list = [1,2,3,4,5,6]
counter = 0
for item in my_list:
    counter = counter + item
print((counter-item),'+',item,'=',counter)
exemplo = 0 + 1 = 1,\
                  1 + 2 = 3,\
                          2 + 4 = 6


for i in range(1,10,2):
        #range(star(inicio),stop(final),step(pulo))
    print(i)

for _ in range(1):
    print(['Wanderson'])

for i,n in enumerate('Wanderson'):
    print(i,n)

colors = [
    'orange',
    'black',
    'purple',
    'white',
    'red',
    'yelow',
    'green'
]
repeat = [1,2,3,4,5]
test = 0
for i in colors:
    for r in repeat:
        ++test
        print(i, r)
print(test)

cad ={
    'name ': 'Wanderson',
    'age  ':1996,
    'magic':True
}
#Print key of array
for key in cad:
    print('Key: ',key)

for i in cad.keys():
    print(i)

#Print values of array
for i in cad.values():
    print('Value: ',i)

#Print values of array
for key,values in cad.items():
    print(key,':',values)
'''

for i,char in enumerate('Wanderson'):
    print(i,char)