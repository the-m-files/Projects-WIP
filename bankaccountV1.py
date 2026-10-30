
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount < 0:
            return "Invalid"
        else:
            self.balance += amount
            self.show_account()

    def withdraw(self, amount):
        if amount > self.balance:
            return False

        self.balance -= amount
        return True

    def show_account(self):
        print(f"Balance: {self.balance}")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount< 0:
            return "invalid balance, has to be positive"
        else:
            self._balance = amount

class SavingAccount(Account):

    def __init__(self, owner, balance, interest):
        super().__init__(owner, balance)
        self.interest = interest

    def add_interest(self):
        self.balance += (self.balance / 100) * self.interest


class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + abs(self.overdraft_limit):
            print("Surpasses overdraft limit, not able to withdraw")
            return False

        self.balance -= amount
        return True

    @Account.balance.setter
    def balance(self, amount):
        if amount < self.overdraft_limit*-1:
            return "invalid account balance"
        else:
            self._balance = amount

class owner:
    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account
        self.history = []

    def display(self):
        self.account.show_account()

    def transfer(self, amount, person):
        if self.account.withdraw(amount):
            self.history.append(f"transfered {amount} to {person.name}")
            person.account.deposit(amount)
            person.history.append(f"recieved {amount} from {self.name}")
            print("Transfer successful")
        else:
            print("Transfer failed")


garys_checking_account = CheckingAccount("Gary", 100, 10)
gary = owner("Gary", 21, garys_checking_account)

martins_saving_account = SavingAccount("Martin", 200, 35)
martin = owner("Martin", 25, martins_saving_account)

martin.transfer(10, gary)
martin.transfer(10031, gary)
print(martin.history)
