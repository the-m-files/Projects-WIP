class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        self.show_account()

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            self.show_account()

        else:
            print("not enough money")

    def show_account(self):
        print(f"Balance:{self._balance}")

    @property
    def balance(self):
        return self._balance



class SavinAccount(Account):
    def __init__(self, owner, balance, interest):
        super().__init__(owner, balance)
        self.interest = interest

    def add_interest(self):
        self.balance += (self.balance/100)*self.interest

class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount > self._balance+abs(self.overdraft_limit):
            print("Surpasses overdraft limit not able to withdraw")
        else:
            self._balance -= amount
            self.show_account()

class owner:
    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account

    def display(self):
        self.account.show_account()

    def transfer(self, amount, person):
        person.account.balance += amount
        self.account.balance -= amount
        print(self.account.balance)
        print(person.account.balance)
    

garys_checking_account = CheckingAccount("Gary", 100, 10)
gary = owner("Gary", 21, garys_checking_account)

martins_checking_account = CheckingAccount("Martin", 200, 35)
martin = owner("Martin", 25, martins_checking_account)


gary.transfer(900, martin)