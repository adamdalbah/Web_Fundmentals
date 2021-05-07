class BankAccount:
    def __init__ (self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
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

alex = BankAccount().deposit(100).deposit(200).deposit(300).withdraw(250).yield_interest().display_account_info()
jack = BankAccount(0.05).deposit(300).deposit(400).withdraw(300).withdraw(100).withdraw(200).withdraw(200).yield_interest().display_account_info()

