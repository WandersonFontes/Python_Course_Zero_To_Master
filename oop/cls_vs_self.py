#self -> reference of instance
#cls -> reference of class
class List:
    my_list = []#Attribute of class

    #Data abstraction manipulation
    @classmethod
    def addList1(cls, obj):
        cls.my_list.append(obj)
        print(cls.my_list)

    #Instance manipulation
    def __init__(self):
        self.new_list = []

    def addList2(self, obj):
        self.new_list.append(obj)
        print(self.new_list)

#numbres = List()
#numbres.addList1(10)
#numbres.addList2(11)

#Other Exemple
class Animal:
    specie = "Mammal"#Attribute Sharing

    def __init__(self):
        self.name = "Lyon"#Attribute Instantiated

my_pet = Animal()
my_pet.specie