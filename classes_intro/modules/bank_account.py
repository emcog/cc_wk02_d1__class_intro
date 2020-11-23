#example function tied to example dictionary
# def get_account_name(account):
    # return account['holder_name']

class BankAccount:
    #self refers to the instance which is being created
    # instance variables – follow self – have scope as long as the class instance is live
    def __init__(self, name, balance, type):
        self.holder_name = name
        self.balance = balance
        #if python runs then it works, in this case ignore syntax highlighting
        self.type = type

    # example behaviour in class
    def pay_in(self, amount):
        self.balance += amount

    # [Task:] Make a pay_monthly_fee method, which reduces the value of the account by 50. Try calling it in `app.py`

    def pay_monthly_fee(self):
        self.balance -= 50