class BankAccount:
    def __init__(self, int_rate, balance=100): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if (self.balance>=amount):
            self.balance-=amount
        else:
            print("insufficient funds")
        return self
    def display_account_info(self):
        print (f"you have {self.balance}")
        return self
    def yield_interest(self, int_rate):
        self.balance+=self.balance * int_rate
        return self

fcu = BankAccount(1.10, 100)
fcu.display_account_info()
fcu.withdraw(25)
fcu.display_account_info()
fcu.deposit(50)
fcu.display_account_info()
fcu.withdraw(250)
fcu.display_account_info()
fcu.deposit(2500)
fcu.display_account_info()
fcu.yield_interest(.06)
fcu.display_account_info().deposit(2000).deposit(2000).yield_interest(.06).display_account_info()