#crie uma classe para implementar uma conta corrente
#atributos: número da conta, número do correntista e saldo
#métodos: alterar nome, depósito e saque
#saldo é opcional
import random

#code

class Account:
    def __init__(self, user_name = None, account_number = None, user_number = None, balance = None):
        self.user_name = user_name
        self.account_number = account_number
        self.user_number = user_number
        self.balance = balance

    def define_name(self):
        self.user_name = input('Enter your name and surname:')

    def accountnumber(self):
        self.account_number = random.randint(10000,99999)
        self.account_number = self.account_number

    def usernumber(self):
        self.user_number = random.randint(1000,9999)
        self.user_number = self.user_number

    def deposit(self):
        deposit1 = int(input('How much do you want to deposit?'))
        self.balance = self.balance + deposit1
        print('Your actual balance is', newaccount.balance)

    def withdrawal(self):
        withdrawal1 = int(input('How much do you want do withdrawal?'))
        self.balance = self.balance - withdrawal1
        if withdrawal1 > self.balance:
            print('ERROR, you dont have that limit.')
        else:
            print('Your actual balance is', newaccount.balance)

    def change_name(self):
        self.user_name = input('Enter your name and surname:')

#instanting
newaccount = Account('Luck', 0, 0, 0)
newaccount.define_name()
print('Welcome to our bank', newaccount.user_name)
newaccount.accountnumber()
newaccount.usernumber()
print(newaccount.user_name, 'your account number is:', newaccount.account_number, 'and your user number is:', newaccount.user_number)
question = int(input('Your actual balance is U$0. Press 1 to do your first deposit, press 0 to exit.'))
if question == 1:
    newaccount.deposit()
elif question == 0:
    print('Thanks, until next time.')
else:
    while (question != 0) or (question!=0):
        question = int(input('Invalid option, press 1 to do your first deposit or 0 to exit'))
        if question == 1:
            newaccount.deposit()
            break
        elif question == 0:
            print('Thanks, until next time.')
            break

action = int(input('What is your next action? 1 - deposit, 2 - withdrawal, 3 - balance, 4 - change your name, 5 - exit'))
if action == 1:
    newaccount.deposit()
elif action == 2:
    newaccount.withdrawal()
elif action == 3:
    print('Your actual balance is', newaccount.balance)
elif action == 4:
    newaccount.change_name()
elif action == 5:
    print('Thanks, until next time.')
else:
    while action in [6,7,8,9]:
        action = int(input('What is your next action? 1 - deposit, 2 - withdrawal, 3 - balance, 4 - change your name, 5 - exit'))
        if action == 1:
            newaccount.deposit()
            break
        elif action == 2:
            newaccount.withdrawal()
            break
        elif action == 3:
            print('Your actual balance is', newaccount.balance)
            break
        elif action == 4:
            newaccount.change_name()
            break
        elif action == 5:
            print('Thanks, until next time.')
            break