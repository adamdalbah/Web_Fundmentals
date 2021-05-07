class User:		# 1- Create a file with the User class, including the __init__ and make_deposit methods:
    def __init__(self,name,email,balance):
        self.name = name
        self.email = email
        self.account_balance =balance

    def deposit(self,amount):
        self.account_balance+=amount
        print(f"Success, you added {amount}\n")
        return self

    #2- Add a make_withdrawal method to the User class:
    def withdrawal(self, amount):
        if amount<=self.account_balance:
            self.account_balance -= amount
            print(f"Success, you withdraw {amount}\n")
        else:
            print(f"You can withdraw at least {self.account_balance}\n")
        return self
    #3- Add a display_user_balance method to the User class:
    def display_user_balance(self):
        print(f"Mr/Ms. {self.name} has a balance of {self.account_balance}")
        return self
    
    def transfer_money (self, other_user, amount):
        self.account_balance -= amount
        other_user.deposit(amount)
        return self
#end of class

#4- Create 3 instances of the User class:
adam = User("Adam","adam@gmail.com",1000).deposit(200).withdrawal(100).display_user_balance()
fatima = User("Fatima", "Fatima@gmail.com",1200).deposit(500).withdrawal(100).transfer_money(adam,200).display_user_balance()
mohammad = User("Mohammad","mohammad@gmail.com",1300).deposit(1000).withdrawal(300).transfer_money(adam, 500)

