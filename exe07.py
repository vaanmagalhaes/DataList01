# crie uma classe que simule um tamagotchi
# atributos: nome, fome, saúde e idade
# métodos: alterar nome, fome, saúde e idade. retornar fome, saúde e idade
# calcular o humor do tamagotchi
from tkinter.font import names


#code
class Tamagotchi:
    def __init__(self, name = None, hunger = None, health = None, age = None, filth = None, fun = None):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.age = age
        self.filth = filth
        self.fun = fun

    def nominate(name):
        name = input('Give a name to your tamagotchi:')
        return name

    def feed(self):
        self.health = self.health + 1


    def medicate(self):
        self.health = self.health + 10


    def bath(self):
        self.filth = self.filth = 0

    def play(self):
        self.hunger = self.hunger - 10
        self.health = self.health - 3
        self.filth = self.filth + 10




newtoy = Tamagotchi('Tamagotchi', 50, 100, 1, 0, 50)
toyname = newtoy.nominate()
print(toyname, 'is waiting for you')


action = input('Press [1] to play, [2] to feed, [3] to medicate, [4] to bath and [5] for humor')
while action == 1:
    newtoy.play()
    if action == 5:
        print(toyname, 'status:', '\n', 'age = ', newtoy.age, '; hunger = ', newtoy.hunger, '; health = ',
              newtoy.health, '; filfh = ', newtoy.filth)
        break
while action == 2:
    newtoy.feed()
    if action == 5:
        print(toyname, 'status:', '\n', 'age = ', newtoy.age, '; hunger = ', newtoy.hunger, '; health = ',
              newtoy.health, '; filfh = ', newtoy.filth)
        break
while action == 3:
    newtoy.medicate()
    if action == 5:
        print(toyname, 'status:', '\n', 'age = ', newtoy.age, '; hunger = ', newtoy.hunger, '; health = ',
          newtoy.health, '; filfh = ', newtoy.filth)
    break

while action == 4:
    newtoy.bath()
    if action == 5:
        print(toyname, 'status:', '\n', 'age = ', newtoy.age, '; hunger = ', newtoy.hunger, '; health = ',
              newtoy.health, '; filfh = ', newtoy.filth)
        break

if action == 5:
    print(toyname, 'status:', '\n', 'age = ', newtoy.age, '; hunger = ', newtoy.hunger, '; health = ', newtoy.health,
          '; filfh = ', newtoy.filth)