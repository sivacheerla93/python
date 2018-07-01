class InsufficientBalance(Exception):
    def __init__(self, balance, w_amount):
        self.message = "Insufficient Balance %d, withdraw amount is %d" % (balance, w_amount)

    def __str__(self):
        return self.message


class Account:
    minbal = 1000

    def __init__(self, acno, customer, balance=0):
        self._acno = acno
        self._customer = customer
        self._balance = balance

    def __str__(self):
        return "{0} {1} {2}".format(self._acno, self._customer, self._balance)

    def withdraw(self, w_amount):
        if self._balance - Account.minbal >= w_amount:
            self._balance -= w_amount
        else:
            raise InsufficientBalance(self._balance - Account.minbal, w_amount)


c1 = Account(555456, "Siva Cheerla", 15000)
print(c1)
try:
    c1.withdraw(15000)
    print("Withdrawn")
except Exception as ex:
    print("Error: ", ex)
