conjunto = {1,2,3,4}
# Conjuntos não podem haver valores duplicados(repetidos)
conjunto.add(5)
conjunto.add(1)
# print(conjunto)


# Podemos remover dados duplicados de uma esturtura colocando dentro du um conjunto
lista = [1,1,2,2,3,3,4,4,5,5]
remove = set(lista)
# print(remove)

# Verificar tamanho do conjunto
print(len(remove))

# Comprehension
# Structure -> [value+1 for value in list]
print('-'*50+f'\nComprehension')

comprehension1 = {i*2 for i in lista}
print(comprehension1)

comprehension2 = {i*2 for i in lista if i >= 4}
print(comprehension2)
