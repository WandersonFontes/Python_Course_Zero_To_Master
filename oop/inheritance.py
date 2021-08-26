#Game Player
class Person:

    def __init__(self, name):
        self.name = name


class Magician:

    def __init__(self, person):
        self.person = person
        Person(self.person)
        print(f'{self.person} is a person of type magician!')

    def create(self):
        print(f"{self.person} is a person of type magician!")

    def attack(self):
        print('Attack: -100')


class Archer:

    def __init__(self, person):
        self.person = person
        Person(self.person)
        print(f'{self.person} now you have a archer!')

    def create(self):
        print(f"{self.person} is a person of type magician!")

    def attack(self):
        print('Attack: -80')


class Ogres:

    def __init__(self, person):
        self.person = person
        Person(self.person)
        print(f'{self.person} a ogre in war!')

    def create(self):
        print(f"{self.person} is a person of type ogre!")

    def attack(self):
        print('Attack: -120')

#newPlayer1 = Magician('Wan')
#newPlayer2 = Archer('Aislan')
#newPlayer3 = Ogres('Toka')

#House
class House:
    def __init__(self):
        print('Welcome your new house!')

    def clear(self):
        print('Cleared sucessfully!')

    def save(self):
        print('Saved sucessfully!')

    def toWash(self):
        print('Washed out sucessfully!')


class Bedroom(House):
    def toSlep(self):
        print('Sleping...')

    def getDressed(self):
        print('Dressing up...')


class Kitchen(House):
    def cook(self):
        print('Cooking...')

    def setTheTable(self):
        print('Setting the table...')


#myBedroom = Bedroom()
#myBedroom.clear()
#myBedroom.toWash()
#myBedroom.toSlep()
myKitchen = Kitchen()

print(isinstance(myKitchen, Kitchen))#True
#Check whether the variable is an instance of a class

print(isinstance(myKitchen, House))#True
#Check whether the variable is an instance of class father







