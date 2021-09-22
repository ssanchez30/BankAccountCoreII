from Account import Account
from User import User

michaelUser = User("Michael", "Miller", "mmiller@yahoo.es")
alvaroUser = User("Alvaro", "Sanchez", "asanchez@gmail.com")
patriciaUser = User("Patricia", "Rojas", "projas@hotmail.com")

michaelAccount = Account(12345, michaelUser, 0.03, 1000)
alvaroAccount = Account(22222, alvaroUser, 0.05, 0)
patriciaAccount = Account(74892, patriciaUser, 0.04, 500)


michaelAccount.make_deposit(1000).make_withdrawal(
    200).make_deposit(3000).make_deposit(500).display_user_balance()

alvaroAccount.make_deposit(3500).make_withdrawal(500).make_withdrawal(
    1500).make_withdrawal(8000).display_user_balance()

patriciaAccount.make_deposit(7000).make_withdrawal(1000).make_withdrawal(
    1900).make_withdrawal(1300).display_user_balance()


print("* BONUS Transfer Michael to Patricia*")
michaelAccount.transfer_money(patriciaAccount, 1000).display_user_balance()
patriciaAccount.display_user_balance()
print("* END BONUS*\n")

print("* SUMMARY REPORT *")
Account.printAllAccountInfo()
