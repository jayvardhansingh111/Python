# Banking application

import sys

class Customer:
    ''' Customer class with bank operations'''

    bankname='DURGABANK'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('The balance after deposit:',self.balance)

    def withdraw(self,amount):
        if amount> self.balance:
            print("Insufficient funds.. cant perform This operation")
            sys.exit()
        self.balance=self.balance-amount
        print("The balance after withdraw:",self.balance)


print("Welcome to",Customer.bankname)
name=input("Enter your name:")
c=Customer(name)
while True:
    print("d-Deposit \n w-Withdraw \n e-exit ")
    opetion=input("choose your option : ")
    if opetion=='d':
        amount=float(input("Enter the amount to deposit:"))
        c.deposit(amount)
    elif opetion=='w':
        while True:
            amount=float(input("Enter amount to withdraw:"))
            if amount>0 and amount%100==0:
               print("Amount should be multiple of hundred")
            else:
                break
        c.withdraw(amount)
    elif opetion=='e':
        print("Thank for using Banking.")
        sys.exit()
    else:
        print("Invalid option.... please enter the valid option")
        print("option are -- d-Deposit \n w-Withdraw \n e-exit ")







