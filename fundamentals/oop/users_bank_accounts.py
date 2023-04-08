class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount, account_name=()):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount, account_name=()):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self, account_name=()):
        print(self.name)
        self.account.display_account_info()
        return self


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
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Total Balance from all accounts: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
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

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

class CheckingAccount(BankAccount):
    def __init__(self, int_rate, balace=0):
        super().__init__(int_rate, balace)
    def write_check(self, amount):
        pass

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance = 0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self


user1 = User("Naomi", "naomi@email.com")
user1.make_deposit(2500,account_name="checking").make_deposit(500,account_name="savings").display_user_balance()

user2 = User("Ginger", "ginger@email.com")
user2.make_deposit(2900,account_name="checking").make_deposit(1000,account_name="savings").display_user_balance().make_withdraw(450,account_name="savings").display_user_balance()

user3 = User("Michael","michael@email.com")
user3.make_deposit(200, account_name="checking").make_deposit(1000,account_name="savings").make_withdraw(400,account_name="checking").display_user_balance()