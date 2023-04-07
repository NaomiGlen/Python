class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []

    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        return self

    def yield_interest(self):
        self.int_rate = self.int_rate * (0.05)
        self.balance += self.int_rate
        return self

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += cls.balance
        return sum

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

account1 = BankAccount(2, 200)
account2 = BankAccount(1, 200)

account1.deposit(200).deposit(100).deposit(400).withdraw(50).yield_interest().display_account_info()
account2.deposit(50).deposit(700).withdraw(80).withdraw(20).withdraw(40).withdraw(100).yield_interest().display_account_info()
