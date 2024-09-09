#criar uma classe macaco
#atributos: nome e bucho
#métodos: comer, verbucho e digerir
#3 alimentos diferentes

#code
class Monkey:
    def __init__(self, name = None, stomach = None):
        self.name = name
        self.stomach = []
    
    def nominate(name):
        name = input('Give a name to your monkey:')
        return name
        
    def feed(self):
        food = input('Choose a fruit to your monkey: banana, watermelon, melon or papaya')
        self.stomach.append(food)
        
    def seeStomach(self):
        for i in self.stomach:
            print(i)
        
    def digest(self):
        self.stomach.clear()
       
        
monkey1 = Monkey('NoName', 'empty')
monkey1_name = monkey1.nominate()
    
action = int(input('Press [1] to feed, [2] to see stomach or [3] to digest'))
while action == 1:
    monkey1.feed()
    action = int(input('Press [1] to feed, [2] to see stomach or [3] to digest'))
while action == 2:
    monkey1.seeStomach()
    print(monkey1_name, 'is feeling full, better digest the food.')
    action = int(input('Press [1] to feed, [2] to see stomach or [3] to digest'))
while action == 3:
    monkey1.digest()
    print('The stomach is empty now.')
    break

question = input('Wanna add another monkey to the cage? [y/n]')
if question == 'y':
    monkey2 = Monkey('NoName', 'empty')
    monkey2_name = monkey2.nominate()
    print('Now', monkey1_name, 'and', monkey2_name, 'are together.')
    
    print('...')
    print('Oh no...')
    print(monkey1_name, 'is too hungry...')
    print('OH GOD. What a relief, they are just playing. Look how cute they are.')
    
    

if question == 'n':
    print('Ok, bye!')