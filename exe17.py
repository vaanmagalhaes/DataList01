# Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles
# através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o
# usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira.
# Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos
#  (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
#  Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de 
#  fome e tédio.

#code
class Tamagotchi:
    def __init__(self, name = None, hunger = None, health = None, bladder = None, age = None, filth = None, fun = None, sleepiness = 0):
        self.name = name
        self.hunger = hunger
        self.health = health
        self.bladder = bladder
        self.age = age
        self.filth = filth
        self.fun = fun
        self.sleepiness = sleepiness

    def nominate(name):
      name = input(f'What do you wanna call your tamagotchi?')
      return name

    def changeName(name):
      name = input(f'Insert the new name:')
      return name

    def medicine(self):
      self.health += 20
      if self. health >= 100:
        print(f'{toyname} looks healthy than ever.')

    def feed(self):
      self.hunger += 10
      self.bladder += 10

    def bath(self):
      self.filth = 0

    def pee(self):
      self.bladder = 0

    def play(self):
      self.fun += 10
      self.sleepiness += 10
      self.health -= 5
      self.bladder += 5
      self.filth += 5
      self.hunger -= -5

    def sleep(self):
      self.sleepiness = 0
      self.hunger = 50
      self.fun = 50
      self.bladder +=5
      print('zZzZzZz....')

    def birthday(self):
      self.age += 1
      print(f'Happy New Year! You missed their birthday!')

newtoy = Tamagotchi('unnamed', 50, 100, 0, 1, 0, 50)
toyname = newtoy.nominate()

newtoy1 = Tamagotchi('unnamed', 40, 100, 10, 2, 30, 5)
toyname1 = newtoy1.nominate()

newtoy2 = Tamagotchi('unnamed', 80, 100, 5, 1, 20, 45)
toyname2 = newtoy2.nominate()

newtoy3 = Tamagotchi('unnamed', 20, 100, 30, 2, 40, 50)
toyname3 = newtoy3.nominate()

newtoy4 = Tamagotchi('unnamed', 100, 80, 10, 1, 25, 50)
toyname4 = newtoy4.nominate()

print(f'Hello! {toyname}, {toyname1}, {toyname2}, {toyname3} and {toyname4} are waiting for you.')


while True:
  action = int(input(f'Now press [1] to play, [2] to feed, [3] to pee, [4] to take a bath, [5] for medication or [6] to sleep. To quit press [0]'))

  if action == 1:
    counter = int(input(f'How many hours you wanna play with them? '))
    for i in range (counter):
      newtoy.play()
      newtoy1.play()
      newtoy2.play()
      newtoy3.play()
      newtoy4.play()
      counter =+ 1
   
  elif action == 2:
    counter = int(input(f'How many fruits you wanna give to them? '))
    for i in range (counter):
      newtoy.feed()
      newtoy1.feed()
      newtoy2.feed()
      newtoy3.feed()
      newtoy4.feed()
      counter =+1
        
  elif action == 3:
    newtoy.pee()
    newtoy1.pee()
    newtoy2.pee()
    newtoy3.pee()
    newtoy4.pee()
    
  elif action == 4:
    newtoy.bath()
    newtoy1.bath()
    newtoy2.bath()
    newtoy3.bath()
    newtoy4.bath()
  
  elif action == 5:
    newtoy.medicine()
    newtoy1.medicine()
    newtoy2.medicine()
    newtoy3.medicine()
    newtoy4.medicine()
  
  elif action == 6:
    newtoy.sleep()
    newtoy1.sleep()
    newtoy2.sleep()
    newtoy3.sleep()
    newtoy4.sleep()
  
  elif action == 0:
    print(f'They are saying goodbye!')
    break

  else:
    print(f'Oh no, you pressed the wrong button. I wonder what will happen to them...')
    newtoy.birthday()
