class FuelPump:
  def __init__(self, fuel = None, price = None, liters = None):
    self.fuel = fuel
    self.price = price
    self.liters = liters

  def fillByValue(self):
    value = int(input('How much dolars you want to pay?'))
    litersBuyed = value / self.price
    self.liters -= litersBuyed
    print(f'You bought {litersBuyed:.2f} liters.')
    print(f'The pump total now is: {self.liters:.2f} liters')

  def fillByLiters(self):
    litersBuyed1 = int(input('How many liters do you want?'))
    totalPrice = litersBuyed1 * self.price
    self.liters -= litersBuyed1
    print(f'You bought {litersBuyed1:.2f} liters by the price of {totalPrice:.2f} dolars')
    print(f'The pump total now is {self.liters:.2f} liters')

pump1 = FuelPump('Gas', 3.52, 10000)
pump1.fillByValue()
  
pump2 = FuelPump('Ethanol', 3.17, 10000)
pump2.fillByLiters()
