import re  # Regex

myPhrase = 'Wanderson is a very skilled and very dedicated developer!'

findIndPhrase1 = re.findall('Wanderson', myPhrase)
print(f'RESULT 1 -> {findIndPhrase1}')

findIndPhrase2 = re.findall('dev', myPhrase)
print(f'RESULT 2 -> {findIndPhrase2}')

findIndPhrase3 = re.findall('a', myPhrase)
print(f'RESULT 3 -> {findIndPhrase3}\nTOTAL -> {str(len(findIndPhrase3))}')

print('-'*50+'\n')
# print(myPhrase)
# search = str(input('Find All: '))
# findIndPhrase4 = re.findall(search, myPhrase)
# if any(findIndPhrase4):
#     print(findIndPhrase4)
# else:
#     print('NO EXIST')

print('-'*50+'\n'+'\nREGEX SEARCH\n')
search1 = re.search('Wanderson', myPhrase)
print(search1)
startInPrase = search1.start()
endInPrase = search1.end()
print(f'Start in: {startInPrase}')
print(f'End in: {endInPrase}')
print(myPhrase[startInPrase:endInPrase])

print('-'*50)

search2 = re.search('developer', myPhrase)
print(search2)
startInPrase = search2.start()
endInPrase = search2.end()
print(f'Start in: {startInPrase}')
print(f'End in: {endInPrase}')
print(myPhrase[startInPrase:endInPrase])

print('-'*50)

# search3 = re.search(str(input('Search: ')), myPhrase)
# if search3 != None:
#     print(search3)
#     startInPrase = search3.start()
#     endInPrase = search3.end()
#     print(f'Start in: {startInPrase}')
#     print(f'End in: {endInPrase}')
#     print(myPhrase[startInPrase:endInPrase])
# else:
#     print('NO EXIST')

print('-'*50+'\n'+'\nREGEX SPLIT\n')

print(myPhrase)
split1 = re.split(' ', myPhrase)
print(split1)

print('-'*50+'\n'+'\nREGEX SUB\n')

print(myPhrase)
sub1 = re.sub('Wanderson ', '', myPhrase)
print(f'RESULT SUB -> {sub1}')




