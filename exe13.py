# Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário)
# e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

#code

class Employee:
  def __init__ (self, name = None, salary = None):
    self.name = name
    self.salary = salary

  def nominateEmployee(self):
    self.name = input('Insert the employees name and surname:')
  
  def paymentCheck(self):
    self.salary = float(input('Enter the employees salary:'))


#instanting
hired = Employee('Name&Surname', 1330)
hired.nominateEmployee()
hired.paymentCheck()
print(f'Welcome to the company, {hired.name}. Your actual salary is U${hired.salary:.2f} dolars.')
