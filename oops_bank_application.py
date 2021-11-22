######Bank application in oops##

import sys
class customer:
    """Customer class with bank related application"""
    bankname="DURGA BANK"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
     
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("After deposit the balance:",self.balance)
       
    def withdraw(self,amt):
        if amt > self.balance:
            print("insufficent funds____canot perform")
            sys.exit()
        else:    
            self.balance=self.balance-amt
            print("After withdraw the Balace:",self.balance)
           
print("Welcome to",customer.bankname)
name=input("Enter your name:")
c=customer(name)
while True:
    print("d-Deposit \nw-Withdraw \ne-Exit")
    option=input("choose your option:")
    if option.lower()=='d':
        amt=float(input("Enter deposit amount:"))
        c.deposit(amt)
    elif option =="w" or option =="W":
        amt=float(input("Enter Withdraw amt:"))
        c.withdraw(amt)
    elif option =="e" or option =="E":
        print("Thanks for banking")
        sys.exit()
    else:
        print("Choose valid option")
        
        
     
        