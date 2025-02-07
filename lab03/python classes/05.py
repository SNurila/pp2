class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit (self):
        print(f"{self.owner} has {self.balance}$ in deposit")

    def withdraw (self, withdraw):
        
        if withdraw > self.balance:
            print("Withdrawal cannot be exceeded")

        else:
            print(self.balance - withdraw)

obj = Account("Corey schafer", 150)
obj.deposit()
obj.withdraw(130)
obj.withdraw(200)