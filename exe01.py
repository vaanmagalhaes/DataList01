#crie uma classe que modele uma bola:
#atributos: cor, circunferência, material
#métodos: trocaCor e mostraCor

#code
class Ball:
    def __init__(self, color = None, circumf = None, material = None):
        self.color = color
        self.circumf = circumf
        self.material = material

    def changecolor(self,color):
        self.color = color

    def showcolor(self):
        print('The new color is:', self.color)


#instantiating

newball = Ball('blue', '8cm', 'leather')
print("The ball color is", newball.color,"its circumference measures",
      newball.circumf, 'and its made of', newball.material)

question = input('Would you like to change the color? [y/n]')

if question == 'y':
    newball.changecolor('green')
    newball.showcolor()
else:
    print('Thats ok, thank u')