class Person:
    genere = None
    name = None
    magician = False

    def __init__(self):
        try:
            print('Person created sucessfuly!')
        except(Exception):
            print('Ops Error!')

    def getGenere(self):
        self.genere = int(input('What your genere?\n0 = Fem\n1 = Masc\nR = '))

    def getName(self):
        self.name = str(input('\nInsert your name, please:\n'))

    def isMagician(self):
        self.magician = bool(input('\nYou is magician?:\n0 = No\n1 = Yes\nR = '))

    def dataPerson(self):
        self.getGenere()
        self.getName()
        self.isMagician()

        print('Data save sucessfuly!')
        print(f'Genere: {"Masc" if self.genere == 1 else "Fem"}\nName: {self.name}\nIs Magician: {"Yes" if self.magician == True else "No"}')

newPerson = Person()
newPerson.dataPerson()
