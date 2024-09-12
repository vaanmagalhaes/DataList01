# Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
# com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure
# tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito)
# que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial
# de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e
# imprime o saldo resultante.

import random

#code

class Account:
    def __init__(self, user_name = None, account_number = None, user_number = None, balance = None, interestRate = None):
        self.user_name = user_name
        self.account_number = account_number
        self.user_number = user_number
        self.balance = balance
        self.interestRate = interestRate

    def defineName(self):
        self.user_name = input('Enter your name and surname:')

    def accountNumber(self):
        self.account_number = random.randint(10000,99999)

    def userNumber(self):
        self.user_number = random.randint(1000,9999)

    def calculateBalance(self):
        for _ in range (5):
          self.balance += self.balance * (self.interestRate/100)
        
#instanting

newaccount = Account('NewClient', 0, 0, 1000, 10)
newaccount.defineName()
newaccount.accountNumber()
newaccount.userNumber()
print(f'Welcome {newaccount.user_name}, your account number is {newaccount.account_number} and your user number is {newaccount.user_number}')
newaccount.calculateBalance()
 
print(f'Your actual balance is U$ {newaccount.balance}')
