#crie uma classe que modele uma pessoa
#atributos: nome, idade, peso e altura
#métodos: envelhecer, engordar, emagrecer, crescer
#menor de 21 anos cresce 0,5cm a cada ano
import math

#code
class Person:
    def __init__(self, name = None, age = None, weigth = None, heigth = None):
        self.name = name
        self.age = age
        self.weigth = weigth
        self.heigth = heigth

    def register(self):
        self.name = input('What is the name you want to give to this person?')

    def defineage(self):
        self.age = int(input('What is the age of this person?'))

    def defineweight(self):
        self.weigth = int(input('What is this person weight? (only numbers)'))

    def defineheigth(self):
        self.heigth = float(input('Whats is this person height?'))

    def birthday(self):
        self.age = self.age + 1
        if self.age <= 21:
            self.heigth = self.heigth + 0.05
            self.heigth = round(self.heigth, 2)
        else:
            self.heigth = self.heigth
            self.heigth = round(self.heigth, 2)

    def eat(self):
        self.weigth = self.weigth + 1

    def diet(self):
        self.weigth = self.weigth - 1



#instanting
newperson = Person('Josh', '28', 1.73, 80)
newperson.register()
newperson.defineage()
newperson.defineweight()
newperson.defineheigth()

print('Happy new year!')
newperson.birthday()
newperson.eat()
print('Now', newperson.name, 'is', newperson.age, 'years old, weighs', newperson.weigth, 'kgs and measures', newperson.heigth, 'meters')

question1 = input('Would you like to continue? [y/n]')
while question1 == 'y':
    newperson.birthday()
    newperson.eat()
    print('Happy new year!')
    print('Now', newperson.name, 'is', newperson.age, 'years old, weighs', newperson.weigth, 'kgs and measures',
          newperson.heigth, 'meters')
    question1 = input('Would you like to continue? [y/n]')
    if (newperson.age >=60) or (question1 == 'n'):
        print('Thats all, folks!')
        break
else:
    print('ERROR, NON-EXISTENT OPTION')