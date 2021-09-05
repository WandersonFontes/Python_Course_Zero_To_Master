import collections
import string

dictionary = {
    'id':1,
    'dev':'Wanderson',
    'ling':'Python',
    'email':'wancf19@gmal.com',
    'alt':1.70
}
# Unlike dictionary data lists they are called by their respective 'dev' keys: behind the value 'Wanderson'
# print(dictionary)
# print(dictionary['dev'],'=',dictionary['email'])

records = {
    'user': ['Wan', 'Aislan', 'Erikles'],
    'number': [1, 2, 3],
    'bool': True
}
print(records['user'])

data = [{
    'user': "Wanderon"
    }, {
    'email': 'wancf19@gmail.com'
    }, {
    'developer': 'Pyton'
    }
]
# print(data[0],data[1])
# Thus, it is not possible to search a dictionary value within the list through the key, but through the list index

# Methods and Functions
data = dict(
    nome='Wanderson',
    email='wancf19@gmail.com'
    )

# Check if you have a certain key inside the dictionary
print('I' in data.keys())
print('Thiago' in data.values())
# print(test)

# Delete all data within the dictionary
# data.clear()
# print(test)
# data.pop('email') # delete the last element from the key
# print(test)


# Copy keys and values ​​to another dictionary
data2 = data.copy()
print(data)
print(data2)

# Change dictionary value
data = dict(
    nome="Wanderson"
)
# data.update({'nome':'Thiago'})

# Change dictionary key
data['user'] = data.pop('nome')
print(data)


# Order Dict
print('-'*50+'\nOrder Dict')

# Preson ('Type'+'Atk'+'Def')
person1 = [("Magican", (30, 40)), ("Archer", (40, 30)), ("Ogre", (90, 90))]
person2 = [("Magican", (30, 40)), ("Archer", (40, 30))]
top = sorted(person1, key=lambda p: p[1][0], reverse=True)
test = collections.OrderedDict(top)
print(f'{person1}\n{top}\n{test}')

# Equality test
a = collections.OrderedDict(person1)
b = collections.OrderedDict(person2)

print(f'Equals: {str(a==b)}')

# Deque
letters = collections.deque(string.ascii_lowercase)

print(len(letters))

print(f'{"-"*50}\n')
for letter in letters:
    print(letter.upper())


print(f'{"-"*50}\nChange Deque')
#Remove
letters.pop()
letters.popleft()

#Insert
letters.append('*')
letters.appendleft('*')
for letter in letters:
    print(letter.upper())