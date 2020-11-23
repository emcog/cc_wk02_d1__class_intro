from modules.bank_account import *

# example data structure
# account = {
#     'holder_name': 'John',
#     'balance': 500,
#     'type': 'business'
# }

# print(get_account_name(account))

# create instance of bank account class
bank_account = BankAccount('John', 500, 'Business')
print(bank_account.holder_name)


bank_account.holder_name = 'Ada'
print(bank_account.holder_name)


bank_account.pay_in(50)
print(bank_account.balance)

bank_account.pay_monthly_fee()
print(bank_account.balance)


bank_account_02 = BankAccount('Robin', 100, 'Personal')
bank_account_02.pay_monthly_fee()
print(bank_account_02.balance)

