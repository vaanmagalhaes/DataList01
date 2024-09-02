#faça um programa que simule um televisor criando-o como um objeto
#atributos: número do canal, aumentar ou diminuir o volume
#número do canal e do volume devem estar dentro da faixa

#code
class Television:
    def __init__(self, channel = None, volume = None):
        self.channel = channel
        self.volume = volume

    def choosechannel(self):
        self.channel = int(input('Choose your channel (only numbers):'))
        print('Now playing channel', newtv.channel)

    def turnup(self):
        self.volume = self.volume + 1
        if self.volume >= 100:
            print('You have reached maximum volume')
        else:
            print(newtv.volume)


    def turndown(self):
        self.volume = self.volume - 1
        if self.volume <= 0:
            print('You have reached minimum volume')
        else:
            print(newtv.volume)

#instating
newtv = Television(0, 10)
newtv.choosechannel()
volume = int(input('Press 0 to exit, press 1 to turn volume up, press 2 to turn volume down'))
if volume == 1:
    newtv.turnup()
elif volume == 2:
    newtv.turndown()
elif volume == 0:
    print(newtv.volume)
else:
    print('invalid option')
while volume:
    int(input('Press 1 to turn volume up, press 2 to turn volume down'))
    if volume == 1:
        newtv.turnup()
    elif volume == 2:
        newtv.turndown()
    elif volume == 0:
        print(newtv.volume)
        break
    else:
        print('invalid option')


# question = int(input('Press 1 to turn volume up, press 2 to turn volume down'))
# if question == 1:
#     newtv.turnup()
# elif question == 2:
#     newtv.turndown()
# else:
#     while (question != 0) or (question != 1):
#         print('Invalid option.')
#         question = int(input('Press 1 to turn volume up, press 2 to turn volume down'))
#         if question == 1:
#             newtv.turnup()
#             break
#         elif question == 2:
#             newtv.turndown()
#             break