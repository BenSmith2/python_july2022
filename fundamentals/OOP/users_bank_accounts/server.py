class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(.02, 150)
    def deposit(self, num):
        self.account.deposit(num)
    def user_info(self):
        print (f"Hello {self.name}")
        return self

class BankAccount:
    accounts=[]
    def __init__(self, int_rate=0.2, balance=100): 
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
    @classmethod
    def list_accounts(cls, account):
        pass

ben = User("Benjamin","ben@email.com")

ben.user_info()
ben.deposit(100)
print(ben.account.balance)