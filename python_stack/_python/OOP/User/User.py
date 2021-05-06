class User:		# 1- Create a file with the User class, including the __init__ and make_deposit methods:
    def __init__(self,name,email,balance):
        self.name = name
        self.email = email
        self.account_balance =balance

    def deposit(self,amount):
        self.account_balance+=amount
        print(f"Success, {self.name} you added {amount}\n")

    #2- Add a make_withdrawal method to the User class:
    def withdrawal(self, amount):
        if amount<=self.account_balance:
            self.account_balance -= amount
            print(f"Success, {self.name} you withdraw {amount}\n")
        else:
            print(f"You can withdraw at least {self.account_balance}\n")

    #3- Add a display_user_balance method to the User class:
    def display_user_balance(self):
        print(f"Mr/Ms. {self.name} has a balance of {self.account_balance}")

    
    def transfer_money (self, other_user, amount):
        self.account_balance -= amount
        other_user.deposit(amount)

#end of class

#4- Create 3 instances of the User class:
adam = User("Adam","adam@gmail.com",1000)
fatima = User("Fatima", "Fatima@gmail.com",1200)
mohammad = User("Mohammad","mohammad@gmail.com",1300)

# 5- Have the first user make 3 deposits and 1 withdrawal and then display their balance:
adam.deposit(300)
adam.deposit(200)
adam.deposit(500)
adam.withdrawal(10000)

#6- Have the second user make 2 deposits and 2 withdrawals and then display their balance:
fatima.deposit(400)
fatima.deposit(400)
fatima.withdrawal(300)
fatima.withdrawal(100)

#7- Have the third user make 1 deposits and 3 withdrawals and then display their balance:
mohammad.deposit(1000)
mohammad.withdrawal(200)
mohammad.withdrawal(100)
mohammad.withdrawal(300)

#8- BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances:
adam.transfer_money(fatima,200)
fatima.display_user_balance()