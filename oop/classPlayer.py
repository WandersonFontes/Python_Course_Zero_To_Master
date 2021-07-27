class Player:#Class
    idPlayer = 0#Object Attribute
    def __init__(self):#Constructor
        self.idPlayer += 1
        print(f'Player {self.idPlayer}')
    def start(self):#Function
        print('Start Game')
    def attack(self, value):
        self.value = value
        print(f'Attack Aplic: {self.value}')
    pass

#print(type(1))
game = Player()#Instance Class Player
#game.start()#Call Function run
print(game.idPlayer)
#game.attack(69)#Call Function run
#help((game))#Show list methods and help