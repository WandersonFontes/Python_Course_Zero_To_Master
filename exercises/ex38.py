#Validador de senhas
#Aula 38
try:
    print('Olá insira seus dados, para que possamos realizar seu cadastro!')
    print('*'*80)
    user = str(input('Digite seu usuário:\n'))
    print('*'*80)
    senha = str(input('Agora vamos cadastrar uma nova senha:\n'))
    print('*'*80)
    senhaN = str(input('Digite a senha mais uma vez: \n'))
    print('*'*80)
    if senha == senha & senhaN>len(4):
        print('A senha foi autorizada!')
    else:
        print('')
except:
    print('')
