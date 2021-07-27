
dictionary = {
    'id':1,
    'dev':'Wanderson',
    'ling':'Python',
    'email':'wancf19@gmal.com',
    'alt':1.70
}
#Diferente das listas dos dados do dicionário são chamandos atevés das sua respctvas chaves 'dev': trás o valor 'Wanderson'
#print(dictionary)
#print(dictionary['dev'],'=',dictionary['email'])

cadastros = {
    'user':['Wan','Aislan','Erikles'],
    'numero':[1,2,3],
    'bool':True
}
print(cadastros['user'])

test = [{
    'user':"Wanderon"
    },{
    'email':'wancf19@gmail.com'
    },{
    'developer':'Pyton'
    }
]
#print(test[0],test[1])
#Dessa forma não é possível buscar um valor do dicionario dentro da lista através da chave e sim através do indice da lista


#Metodos e funções
test = dict(nome='Wanderson',
            email='wancf19@gmail.com'
            )
#Verificar se tem uma determinada chave dentro do dicionario
print('Eu' in test.keys())
print('Thiago' in test.values())
#print(test)

#Apagar todos os dados dentro do dicionario
#test.clear()
#print(test)
#test.pop('email') #exclui o ultimo elemnto a partir da chave
#print(test)


#Fazer copia das chave e valores para outro dicionario
test2 = test.copy()
print(test)
print(test2)

#Mudar valor do dicionario
test = dict(
    nome="Wanderson"
)
#test.update({'nome':'Thiago'})



#Mudar chave do dicionario
test['user'] = test.pop('nome')

print(test)
