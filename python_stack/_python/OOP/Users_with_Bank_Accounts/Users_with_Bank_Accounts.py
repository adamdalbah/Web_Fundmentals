class BankAccount:
    def __init__ (self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount = 0):
        self.balance += amount
        return self

    def withdraw(self, amount = 0):
        if self.balance >= amount:   
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self


    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0 :
            self.balance += self.balance * self.int_rate
        return self

class User:		# 1- Create a file with the User class, including the __init__ and make_deposit methods:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)
        self.account_2 = BankAccount(0.02, 0) 
        self.account_3 = BankAccount(0.02, 0)

    def deposit(self):
        self.account = self.account.deposit()
        self.account_2 = self.account_2.deposit()
        self.account_3 = self.account_3.deposit


    #2- Add a make_withdrawal method to the User class:
    def withdrawal(self):
        self.account = self.account.withdraw()

    #3- Add a display_user_balance method to the User class:
    def display_user_balance(self):
        self.account.display_account_info



