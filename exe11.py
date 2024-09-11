class Cars:
    def __init__(self, km = None, tank = None):
      self.km = km
      self.tank = tank

    def move(self):
      distance = int(input('What is the distance we are moving? In km.'))
      consumption = distance / 4
      if consumption > self.tank:
        print('You dont have enough fuel to complete the trip.')
        return
      self.km += distance
      self.tank -= consumption
      
    def fillUp(self):
      fill = int(input('How many liters of gas you wanna buy?'))
      self.tank += fill
            
    def showTank(self):
      print(f'The current tank level is: {self.tank:.2f} liters and the odometer is in {self.km:.1f} kms')

RandRover = Cars(0, 0)
RandRover.fillUp()
RandRover.move()
RandRover.showTank()
