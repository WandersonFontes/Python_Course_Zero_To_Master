'''
yes = False
ok = True
no = False
#and, or são operadores lógicos
if yes or ok: # se alguma das duas váriaves for verdadeira irá fazer o comando que está dentro do bloco
    print("Your afimative is true!")
else:# Senão irá executar o código desse bloco
    print('Your afirmative is false!')


n1 = 1
n2 = n1
if n1 == 1 and n2 == 1:
    print('O valor dentro da váriavel é 1!')
else:
    print('O valor está incorreto')
'''
magic = True
expert = True
print('Are you master magic?')
if magic and expert:
    print('Yes! Master Magic.')
elif magic or expert:
    print('Are you magic, do not master')
else:
    print('No magic!')

