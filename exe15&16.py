# Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique
# quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
# Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

# Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto.
# Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário.
# Dica: acrescente um método especial str() à classe Bichinho.

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
      print(f'Happee birthdae, {toyname}. Now you are {self.age}!')

#instanting 

newtoy = Tamagotchi('unnamed', 50, 100, 0, 1, 0, 50)
toyname = newtoy.nominate()
question1 = int(input(f'Are you happy with your choice? Press [1] to confirm or [2] to change. '))
while question1 == 2:
  toyname = newtoy.changeName()
  question1 = int(input(f'Are you happy with your choice? Press [1] to confirm or [2] to change.'))
  if question1 == 1:
    break

print(f'Hello, {toyname} is waiting for you.')

while True:
  action = int(input(f'Now press [1] to play, [2] to feed, [3] to pee, [4] to take a bath, [5] for medication, [6] to sleep or [7] to see {toyname} status. To quit press [0]'))

  if action == 1:
    counter = int(input(f'How many hours you wanna play with {toyname}? '))
    for i in range (counter):
      newtoy.play()
      counter =+ 1
      if newtoy.sleepiness == 100:
          print(f'{toyname} is tired right now. You better put him to sleep.')
          break      
      if newtoy.bladder == 90:
          print(f'{toyname} wants to use the bathroom.')
          break
      if newtoy.hunger == 30:
          print(f'{toyname} is feeling hungry. You better feed him.')
          break
      if newtoy.fun == 100:
        print(f'{toyname} is having so much fun, give him some time to rest...')
        
  elif action == 2:
    counter = int(input(f'How many fruits you wanna give to {toyname}? '))
    for i in range (counter):
      newtoy.feed()
      counter =+1
      if newtoy.hunger == 100:
          print(f'{toyname} is full right now, you cant give him more food.')
          break
      if newtoy.bladder == 90:
          print(f'{toyname} wants to use the bathroom.')
          break
        
  elif action == 3:
    newtoy.pee()
    
  elif action == 4:
    newtoy.bath()
  
  elif action == 5:
    newtoy.medicine()
  
  elif action == 6:
    newtoy.sleep()
  
  elif action == 7:
    print(f'{toyname} actual status is: hunger: {newtoy.hunger}, health: {newtoy.health}, bladder: {newtoy.bladder}, filth: {newtoy.filth}, fun: {newtoy.fun} and sleepiness: {newtoy.sleepiness} ')

  elif action == 0:
    print(f'{toyname} says bye!')
    break

  else:
    print(f'Oh no, you pressed the wrong button. I wonder what will happen to {toyname}...')
    newtoy.birthday()
