class Account:
    # class attribute or static attribute
    minbal = 1000
    # To get no of objects of a class
    numOfInstances = 0

    def __init__(self, acno, customer, balance=0):
        self.__acno = acno
        self.__customer = customer
        self.__balance = balance
        # To get no of objects of a class
        Account.numOfInstances += 1

    def __del__(self):
        Account.numOfInstances -= 1

    def print(self):
        print("Account no: ", self.__acno)
        print("Customer name: ", self.__customer)
        print("Account balance: ", self.__balance)

    def __str__(self):
        return "{0} {1} {2}".format(self.__acno, self.__customer, self.__balance)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return print(amount, "deposited successfully! to account number", self.__acno, "Available balance is: ",
                     self.__balance)

    def withdraw(self, amount):
        if self.__balance - Account.minbal >= amount:
            self.__balance -= amount
            return print(amount, "has been withdrawn! from account number", self.__acno, "Available balance is: ",
                         self.__balance)
        else:
            return print("Insufficient balance to withdraw from your account number", self.__acno,
                         " Available balance is: ",
                         self.__balance)

    def __eq__(self, other):
        return self.__acno == other.__acno and self.__balance == other.__balance

    @staticmethod
    def set_minbal(new_minbal):
        Account.minbal = new_minbal

    @staticmethod
    def get_instances():
        return Account.numOfInstances


# objects
# we can set minbal from here using static method
Account.set_minbal(500)
c1 = Account(123456, "Siva", 1500)
c1.print()
print()
c2 = Account(123457, "Raju", 1500)
c2.print()
print()
print("String of c1 is: ", str(c1))
print()
print("Balance of c2 is: ", c2.get_balance())
print()
c1.deposit(5000)
c1.deposit(2500)
c1.withdraw(3500)
c2.withdraw(1000)
c2.withdraw(100)
print(c1 == c2)
print(c1.get_balance())
print(c2.get_balance())
c2.deposit(5000)
print()
print(c1.__dict__)
print(c2.__dict__)
print(Account.__dict__)
print("No. of objects present in the Account class are: ", Account.get_instances())
del c2
print(Account.get_instances())
