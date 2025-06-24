class bank_account:
    def __init__(self, balance):
        self.__balance = balance
    def deposite(self, amount):
        self.__balance = self.__balance + amount
    def withdaw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance -amount
            return True
        else:
            return False
    def get_balance(self):
        return self.__balance

pooja = bank_account(1000)
pooja.get_balance()
pooja.deposite(1500)
pooja.get_balance()
pooja.withdaw(5000)
pooja.withdaw(500)
pooja.get_balance()
