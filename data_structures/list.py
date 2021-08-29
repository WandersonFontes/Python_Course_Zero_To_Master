'''
lista1 = [1,2,3,4,5]
lista2 = ["Wanderson","da","Cunha","Fontes"]
lista3 = ['Wanderson', 23, True]
'''
#As lista podem conter dados de diferentes tipos
#Os dados são organizados e localizados através de indexão

#print(lista2[0::3])
#Pular indices dentro da lista [inicio:final:indíce]

#lista3[0]= 'Thiago'

'''
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[1][2])
#Printa na tela a linha e coluna especificada 
'''


print(50*'*','Criando e adicionando valores em estruturas de Listas',50*'*')
lista = ['Wanderson','Thiago', 'Navarro']
email = ['wancf19@gmail.com', 'wanderson@dataautomacao.com']

#Adicionar u valor no final da lista
lista.append('Wanderson')
email.append('wancf19@gmail.com')

lista.insert(1,'Fontes')
#Inserir valor com um indice especifico da lista
#list(index,value)


lista.insert(1,'da')

new_list=lista,email
print(lista)
print(new_list)#Exibição de uma lista dentro da outra


print('Tamanho da lista: LISTA(',len(lista),')')#tamanho da lista
print('Tamanho da lista: NEW_LIST(',len(new_list),')')

print('O endereço do dados DA esta na seguinte posição da lista:',lista.index('da'))#Endereço de locação da lista
print('O endereço do email está na seguinte posição da lista:',email.index('wancf19@gmail.com'))

print(50*'*','Remoção dos elementos das LISTAS',50*'*')
#new_list.clear()    #APAGAR TODOS OS DADOS DENTRO DA LISTA
print(new_list)


new_list = lista.index('da', 0, 2)



print(new_list)
# Método para verificar se o valor está dentro da lista ou não
print('Cunha' in lista)
# Método para verifocar quantas vezes um dados se repete dentro da lista
print(lista.count('da'))

num = [1,2,3,5,4,7,6,8]
alf = ['a','c','b','e','d']
# Método para fazer ordenação dos valores de uma lista
alf.sort()
# SORTED(LISTA) Outra forma de colocar em oredem os valores da lista
print('SORTED =  ',sorted(num),'\nSORTED =  ',alf)
#RESVERSE atributo para reverter os valores da lista
num.reverse()
print(f'REVERSE =  {num}!')

divisor = '*'
test = divisor.join(lista)
test1 = ' '.join(lista)
print(test)
print(test1)

#Methods Iterabbles
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






