#Methods of Instance
#Só funcionam com a classe instanciada
#Manipulam atributos da instância

#Methods of Class
#Funcionam em todos os momentos
#Manipulam os atributos da classe

#Methods Static
#Funcionam em todos os momentos
#Não manipulam os atributos da classe

#Methods Abstratic
#Metódos que podem ser usados

class Pizza:
    slices = 8

    # Methods of Class
    @classmethod
    def changeSlices(cls, slices):
        cls.slices = slices

    def __init__(self, flavor):
        self.flavor = flavor
        self.preparationTime(self)

    def eatSlice(self):
        self.slices = self.slices-1
        print(self.slices)

    @staticmethod
    def preparationTime(self):
        print('Loandig\n')
        print('1\n')
        print('2\n')
        print('3\n')
        print('Finished!')



myPizza = Pizza('Portuguese')
print(myPizza.slices)
myPizza.eatSlice()

