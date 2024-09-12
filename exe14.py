# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento)
# que aumente o salário do funcionário em uma certa porcentagem.
# Exemplo de uso: harry=funcionário("Harry",25000) harry.aumentarSalario(10)

#code

class Employee:
  def __init__ (self, name = None, salary = None):
    self.name = name
    self.salary = salary

  def nominateEmployee(self):
    self.name = input('Identify the employees using name and surname:')
  
  def paymentCheck(self):
    self.salary = float(input('Enter the employees actual salary:'))

  def promotion(self):
    percentage = int(input('Inform the percentage of the salary increase:'))
    self.salary += self.salary * (percentage/100)


#instanting
hired = Employee('Name&Surname', 1330)
hired.nominateEmployee()
hired.paymentCheck()
hired.promotion()
print(f'Hello, {hired.name}! Congratulations on your promotion, your new salary is U${hired.salary:.2f} dolars.')
