class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info (self):
        return(f"Balance:{self.balance}")

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self 



class user:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02, 9000),
            "savings" : BankAccount (.05, 10000)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
    
    def transfer_money(self,amount,User): 
        self.amount -= amount
        User.amount += amount
        self.display_user_balance()
        user.display_user_balance()

Jessica = user("Jessica")

Jessica.account['checking'].deposit(100)
Jessica.display_user_balance()
