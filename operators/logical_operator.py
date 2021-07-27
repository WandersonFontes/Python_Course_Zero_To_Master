is_magican = True
is_necromanter = input('Is Necromanter? ')
booksBlack = input('Do you have Black Books? ')

if is_magican or is_necromanter:
    print('Magican weak!')
if is_magican and is_necromanter:
    print('Magican trong!')
if is_magican and is_necromanter and booksBlack:
    print('You are magican powerful!')