#crie uma classe que modele um quadrado:
#atributos: tamanho do lado
#métodos: mudar valor do lado, retornar valor do lado e calcular área

#code
class Square:
    def __init__(self, size = None):
        self.size = size

    def changesize(self):
        self.size = int(input('input the new size:'))

    def showsize(self):
        print('The new size is:', self.size)

    def calculatearea(self):
        print('The area size is:', self.size ** 2)

#instanting
newsquare = Square (5)
print('The square size:', newsquare.size)

question = input('Would you like to change the size? [y/n]')
if question == 'y':
    newsquare.changesize()
    newsquare.showsize()
    question2 = input('Would you like to calculate the square area? [y/n]')
    if question2 == 'y':
        newsquare.calculatearea()
    else: print('Ok, bye')
else:
    question3 = input('Would you like to calculate the square area? [y/n]')
    if question3 == 'y':
        newsquare.calculatearea()
    else:
        print('Ok, bye!')
