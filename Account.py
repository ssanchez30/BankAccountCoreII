
class Account:
    bankName = "Coding Dojo Bank"
    allBankAccounts = []

    def __init__(self, accountNum, user, int_rate=0.01, balance=0.0):
        self.accountNum = accountNum
        self.user = user
        self.int_rate = int_rate
        self.balance = balance

        Account.allBankAccounts.append(self)

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("We cannot process your withdrawal.")
            print(f"You currently have {self.balance}.")
            print(f"And you are trying to withdraw {amount}.")
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def display_user_balance(self):
        self.user.printUserInfo()
        print(f"Account number #:{self.accountNum}.")
        print(f"Account balance $:{self.balance}.\n")
        return self

    @classmethod
    def changeBankName(cls, newName):
        cls.bankName = newName

    @classmethod
    def printAllAccountInfo(cls):
        for account in cls.allBankAccounts:
            account.display_user_balance()

    @staticmethod
    def doesAccountHasMoreThan1000(account):
        if(account.balance >= 1000):
            return True
        else:
            return False

    def validateFunds(self, amount):
        if self.balance > amount:
            return True
        else:
            return False

    def transfer_money(self, externalAccount, amountToTransfer):
        if self.validateFunds(amountToTransfer):
            self.make_withdrawal(amountToTransfer)
            externalAccount.make_deposit(amountToTransfer)
        else:
            print("You don't have enough funds to transfer.")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance*self.int_rate
            self.balance += interest
        return self
