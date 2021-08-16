#Encapsulation
class Project:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def data_project(self):
        print(f"Project of software named {self.name}!")

new = Project('New_Project', 100)

other = {'name':'Other_Project', 'value':99}

#print(new.name, new.value)
#print(other['name'], other['value'])

#Abstraction
#refers to an entity that can be anything
#Process and Datas

#Process Abstraction
#It is not so relevant what happens in some background functions if it is called and executed as desired
print('Process Abstraction')
print(f"len -> {len([9,7,1,3,4,5,2,8,6])}\nsorted -> {sorted([9,7,1,3,4,5,2,8,6])}\npop -> {[9,7,1,3,4,5,2,8,6].pop(8)}")
print(f"upper -> {('WanDevNinja').upper()}")
print('-'*50)

#Data Abstration
#Forms used for a data representation
print('Data Abstration')
print('int -> Data of type integer\nbool -> True or False\nstr -> Data of type text\nfloat -> Data of type decimal')


