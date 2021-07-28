class Animal():
    def specie(self):
        print('Mamifero')
    @classmethod
    def test_of_class_method(cls, n1, n2):
        print(n1+n2)
    @staticmethod
    def test_of_static_method(n1, n2):
        print(n1 + n2)

instanci = Animal()
instanci.specie()
instanci.test_of_class_method(2,3)
instanci.test_of_static_method(2,3)

