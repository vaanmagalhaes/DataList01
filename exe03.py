#crie uma classe que modele um retangulo
#atributos: Comprimento, Largura
#métodos: mudar valor dos lados, retornar o valor dos lados, calcular area
#calcular perimetro
#crie um programa que utilize esta classe, ele deve permitir ao usuário
#informar a medida de um local, depois deve criar um objeto com
#as medidas e calcular a quantidade de pisos e de rodapés necessárias
#para o local:
import math

#code
class Rectangle:
    def __init__(self, length = None, width = None):
        self.length = length
        self.width = width

    def changelength(self):
        self.length = int(input('What is the tile length (centimeters)?'))

    def changewidth(self):
        self.width = int(input('What is the tile width (centimeters)?'))

#instanting
newrectangle = Rectangle(None, None)
newrectangle.changelength()
newrectangle.changewidth()
question1 = input('Is this your tile size? [y/n]')
while question1 == 'n':
    newrectangle.changewidth()
    newrectangle.changelength()
    question2 = input('Is this your tile size? [y/n]')
    if question2 == 'y':
        print('Starting program...')
        break
else:
    print('Starting program...')

localwidth = int(input('Enter your local width: [METERS IN NUMBERS]'))
localwidth = localwidth * 100
locallength = int(input('Enter your local length: [METERS IN NUMBERS]'))
locallength = locallength * 100
localtype = input('Choose the ambient type: 1 - square, 2 - rectangle, 3 - triangle')
if localtype == '1':
    localarea = localwidth*2
elif localtype == '2':
    localarea = locallength*localwidth
elif localtype == '3':
    localarea = (localwidth*locallength)/2
else:
    while localtype in ['4','5','6','7','8','9']:
        print('Enter a valid value:')
        localtype = input('Choose the ambient type: 1 - square, 2 - rectangle, 3 - triangle')

tilearea = newrectangle.length * newrectangle.width
result = (localarea / tilearea)
margem = (result*0.15) + result
margem = math.ceil(margem)
print('You will need', margem, 'tiles')