class BankAccount:
    #self refers to the instance which is being created
    # instance variables – follow self – have scope as long as the class instance is live
    def __init__(self, name, balance, type):
        self.holder_name = name
        self.balance = balance
        #if python runs then it works, in this case ignore syntax highlighting
        self.type = type

#example function tied to example dictionary
# def get_account_name(account):
    # return account['holder_name']